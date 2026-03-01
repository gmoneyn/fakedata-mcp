# fakedata-mcp

Generate realistic fake data for testing and development. Create users, companies, transactions, addresses, and custom datasets in JSON or CSV format.

## Install

```bash
uvx fakedata-mcp
```

Or install permanently:

```bash
pip install fakedata-mcp
```

## Tools

- **generate_users** — Generate realistic fake user profiles with name, email, phone, address, date of birth, and username
- **generate_companies** — Generate fake company profiles with name, industry, revenue, employee count, founded date, and website
- **generate_transactions** — Generate fake financial transactions with amount, date, merchant, category, payment method, and status
- **generate_addresses** — Generate fake street addresses with street, city, state, zip, country, and coordinates
- **generate_text** — Generate placeholder text: lorem ipsum paragraphs, realistic sentences, or random words
- **generate_dataset** — Generate a custom dataset with user-defined columns and types. Supports: string, integer, float, boolean, email, name, phone, date, url, uuid, ip_address, color, company, job_title

## Usage with Claude Code

```bash
claude mcp add fakedata-mcp -- uvx fakedata-mcp
```

Or add to your MCP config (`~/.claude/settings.json`):

```json
{{
  "mcpServers": {{
    "fakedata-mcp": {
      "command": "uvx",
      "args": ["fakedata-mcp"]
    }}
  }}
}}
```

## Development

```bash
git clone https://github.com/YOUR_USERNAME/fakedata-mcp.git
cd fakedata-mcp
uv venv .venv && source .venv/bin/activate
uv pip install -e ".[dev]"
pytest -v
```
