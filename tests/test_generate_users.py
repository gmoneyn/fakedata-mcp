"""Test generate_users tool."""

import json

from fakedata_mcp.tools.generate_users import generate_users


def test_generate_users_returns_json():
    result = generate_users(count=1, locale="test", fields="test")
    data = json.loads(result)
    assert isinstance(data, dict)
