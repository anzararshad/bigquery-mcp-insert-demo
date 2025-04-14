# 🧪 BigQuery Data Writer MCP

This project allows you to use **Claude** to generate sample data and automatically write it to **Google BigQuery** using the **Model Context Protocol (MCP)** server.

It's a handy way to prototype, test, or bootstrap your pipelines with realistic datasets.

---

## 🚀 What It Does

- Let Claude create BigQuery tables with custom schemas
- Allows Claude to insert data directly into those tables
- Great for generating test data, prototyping ideas, or populating sample datasets for LLM/RAG training and experimentation

---

## 📋 Requirements

- Python 3.13+
- Google Cloud project with BigQuery enabled
- A service account key with BigQuery access
- Claude Desktop installed and running locally

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anzararshad/bigquery-mcp-insert-demo.git
   cd bigquery-mcp-insert-demo
   ```

2. Install dependencies using [UV](https://github.com/astral-sh/uv):

   ```bash
   uv venv
   uv sync
   ```

3. Set up your Google Cloud service account:

   - Create a service account with BigQuery Admin/Editor roles
   - Download the JSON key file
   - Save it in a `secret/` folder and configure the path in `main.py`

---

## ⚙️ Configuration

Edit `main.py` to add your project and dataset info:

```python
PROJECT_ID = "your-gcp-project-id"
DATASET_ID = "your-bigquery-dataset"
SERVICE_ACCOUNT_FILE = "./secret/your-service-account-key.json"
```

Ensure the dataset exists in your project. Create it via the BigQuery Console or CLI if not.

---

## 🏃 Running the MCP Server

To register the BigQuery writer tool with Claude:

```bash
uv run mcp install main.py
```

Expected output:

```
INFO     Added server 'BigQueryReadWriter' to Claude config
INFO     Successfully installed BigQueryReadWriter in Claude app
```

This means the MCP server is now available to Claude Desktop.

---

## 🤖 Example Prompt to Use with Claude

Ask Claude to create and populate a table using this kind of prompt:

```
I’m working on a dataset around tech startups and their funding history. Can you generate a sample data row for startups that recently raised funding?

Please respond in JSON format with these fields:
* "table_id": a string for the BigQuery table name.
* "schema": a list of columns, where each column is a JSON object with:
   * "name": the column name
   * "type": BigQuery data type (STRING, INT64, FLOAT64, BOOL, TIMESTAMP, etc.)
   * "description": a short description of the column
* "data": a single JSON object with values that match the schema.

Include fields like:
- startup_name
- industry
- funding_stage (like Seed, Series A, Series B, etc.)
- amount_raised_usd
- lead_investor
- founded_year
- is_profitable (boolean)
- headquarters_country
- funding_date (timestamp)

Note: Project ID and dataset are already configured, no need to include them.

```

Claude will then:
- Define a schema
- Generate mock data
- Call the `BigQueryReadWriter` tool via MCP
- Create the table and insert the data into BigQuery 🎯

---

## 📚 References

- [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)
---

## 🧠 Why I Built This

As someone who works with both data and ML, I often need sample datasets to test pipelines, train models, or prep for a RAG setup. Instead of manually writing mock data every time, I figured — why not ask Claude to generate it for me, *and* push it into BigQuery directly?

This tool saves me time, and maybe it’ll save you some too. Feel free to fork, tweak, and adapt it to your needs. Drop a ⭐ if it helps you!

---
