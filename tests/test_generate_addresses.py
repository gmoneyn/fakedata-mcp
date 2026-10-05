"""Test generate_addresses tool."""

import json

from fakedata_mcp.tools.generate_addresses import generate_addresses


def test_generate_addresses_returns_json():
    result = generate_addresses(count=1, country="test")
    data = json.loads(result)
    assert isinstance(data, dict)
