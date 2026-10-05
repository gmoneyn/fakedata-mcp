"""Transport helpers for fakedata-mcp."""

import sys


def run_stdio(mcp_app):
    """Run the MCP server over stdio (default for Claude Code / Cursor)."""
    mcp_app.run(transport="stdio")
