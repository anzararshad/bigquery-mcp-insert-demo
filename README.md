# BigQuery Data Writer for Claude

This project lets you use Claude to generate sample data and automatically insert it into Google BigQuery tables. It uses the MCP (Model Completion Provider) Server to create a tool that Claude can use to interact with BigQuery.

## 🚀 What it does

- Allows Claude to create BigQuery tables with custom schemas
- Enables Claude to insert data directly into those tables
- Perfect for quickly generating test datasets, sample data, or prototyping

## 📋 Requirements

- Python 3.13+
- Google Cloud account with BigQuery access
- Service account credentials with BigQuery permissions
- Claude Desktop Installed 

## 🔧 Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/mcp-bigquery.git
   cd mcp-bigquery
   ```

2. Install the required dependencies(use UV):
   ```
   uv pip install -e .
   ```

3. Set up your Google Cloud service account:
   - Create a service account with BigQuery access
   - Download the JSON key file
   - Save it in the `secret` folder (or update the path in `main.py`)

## ⚙️ Configuration

Edit the `main.py` file to update your configuration:

```python
# Setup
PROJECT_ID = "your-gcp-project-id"
DATASET_ID = "your-bigquery-dataset"
SERVICE_ACCOUNT_FILE = "/path/to/your-service-account-key.json"
```

Make sure the dataset exists in your BigQuery project, or create it before running the tool.

## 🏃‍♂️ Running the MCP Server

Start the MCP server:

```
uv run mcp install main.py  
```

You should see below in console:
```
INFO     Added server 'BigQueryReadWriter' to Claude config                                                                                       claude.py:129
INFO     Successfully installed BigQueryReadWriter in Claude app                                                                                     cli.py:467
```
now the mcp server will be get added to claude desktop

1. The tool accepts a payload with:
   - `table_id`: The name for the BigQuery table
   - `schema`: A list of column definitions with name, type, and description
   - `data`: A dictionary/row of data matching the schema

## 📝 Example Usage with Claude

Here's a sample prompt you can use with Claude:
I need to create a table with country population and household data. Can you generate realistic data for at least 10 countries? 

```Please use the write_to_bigquery tool to:
1. Create a table named "global_demographics" 
2. Include fields for country name, population, households, continent, population density, and avg household size
3. Generate realistic data for at least 10 diverse countries across different continents

The response must be in JSON format with:
- "table_id": the name for the BigQuery table
- "schema": list of column definitions (name, type, and description for each)
- "data": a JSON object with values matching the schema

Remember that the Project ID and dataset are already configured in the tool.
```
Claude will respond with the appropriate JSON structure and use the BigQueryReadWriter tool to create the table and insert the data.

## 📚 Resources

- [MCP Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
