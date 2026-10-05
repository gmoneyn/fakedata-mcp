"""MCP server for fakedata-mcp."""

from mcp.server.fastmcp import FastMCP

# --- IMPORTS ---
from fakedata_mcp.tools.generate_users import generate_users as _generate_users_impl
from fakedata_mcp.tools.generate_companies import generate_companies as _generate_companies_impl
from fakedata_mcp.tools.generate_transactions import generate_transactions as _generate_transactions_impl
from fakedata_mcp.tools.generate_addresses import generate_addresses as _generate_addresses_impl
from fakedata_mcp.tools.generate_text import generate_text as _generate_text_impl
from fakedata_mcp.tools.generate_dataset import generate_dataset as _generate_dataset_impl
# --- END IMPORTS ---

mcp = FastMCP("fakedata-mcp")

# --- TOOLS ---

@mcp.tool(description="Generate realistic fake user profiles with name, email, phone, address, date of birth, and username")
def generate_users(count: int = 5, locale: str = "en_US", fields: str = "") -> str:
    """Call the generate_users tool."""
    return _generate_users_impl(count, locale, fields)

@mcp.tool(description="Generate fake company profiles with name, industry, revenue, employee count, founded date, and website")
def generate_companies(count: int = 5, industry: str = "") -> str:
    """Call the generate_companies tool."""
    return _generate_companies_impl(count, industry)

@mcp.tool(description="Generate fake financial transactions with amount, date, merchant, category, payment method, and status")
def generate_transactions(count: int = 10, min_amount: float = 1.0, max_amount: float = 1000.0, currency: str = "USD") -> str:
    """Call the generate_transactions tool."""
    return _generate_transactions_impl(count, min_amount, max_amount, currency)

@mcp.tool(description="Generate fake street addresses with street, city, state, zip, country, and coordinates")
def generate_addresses(count: int = 5, country: str = "US") -> str:
    """Call the generate_addresses tool."""
    return _generate_addresses_impl(count, country)

@mcp.tool(description="Generate placeholder text: lorem ipsum paragraphs, realistic sentences, or random words")
def generate_text(type: str = "lorem", count: int = 3) -> str:
    """Call the generate_text tool."""
    return _generate_text_impl(type, count)

@mcp.tool(description="Generate a custom dataset with user-defined columns and types. Supports: string, integer, float, boolean, email, name, phone, date, url, uuid, ip_address, color, company, job_title")
def generate_dataset(columns: str, rows: int = 10, format: str = "json") -> str:
    """Call the generate_dataset tool."""
    return _generate_dataset_impl(columns, rows, format)
# --- END TOOLS ---


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
