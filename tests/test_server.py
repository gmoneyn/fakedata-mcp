"""Test that all tools are registered on the MCP server."""

from fakedata_mcp.server import mcp


def test_tools_registered():
    tool_names = set(mcp._tool_manager._tools.keys())
    expected = {"generate_users", "generate_companies", "generate_transactions", "generate_addresses", "generate_text", "generate_dataset"}
    assert expected.issubset(tool_names), f"Missing tools: {expected - tool_names}"
