"""Test generate_companies tool."""

import json

from fakedata_mcp.tools.generate_companies import generate_companies


def test_generate_companies_returns_json():
    result = generate_companies(count=1, industry="test")
    data = json.loads(result)
    assert isinstance(data, dict)
