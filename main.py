from mcp.server.fastmcp import FastMCP
from google.cloud import bigquery
from google.oauth2 import service_account
from google.api_core.exceptions import NotFound

# Setup
PROJECT_ID = "staging-env-449414"
DATASET_ID = "biguqery_mcp"
SERVICE_ACCOUNT_FILE = "/Users/arshad1996/Desktop/my_github/bigquery-mcp-insert-demo/secret/staging-env-449414-bd729276d3a7.json"

mcp = FastMCP("BigQueryReadWriter")

@mcp.tool()
def write_to_bigquery(payload: dict) -> str:
    """
    Accepts payload from Claude with:
    - table_id: str
    - schema: list of {"name", "type", "description"}
    - data: dict matching schema
    """
    try:
        table_id = payload["table_id"]
        schema_info = payload["schema"]
        row_data = payload["data"]
        full_table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_id}"

        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
        client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

        # Check if table exists
        try:
            client.get_table(full_table_id)
        except NotFound:
            schema = [
                bigquery.SchemaField(col["name"], col["type"], description=col.get("description", ""))
                for col in schema_info
            ]
            table = bigquery.Table(full_table_id, schema=schema)
            client.create_table(table)

        # Insert row
        errors = client.insert_rows_json(full_table_id, [row_data])
        if errors:
            return f"Failed to insert: {errors}"
        return f"Successfully inserted into {full_table_id}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
