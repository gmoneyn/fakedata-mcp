"""Test generate_text tool."""

import json

from fakedata_mcp.tools.generate_text import generate_text


def test_generate_text_returns_json():
    result = generate_text(type="test", count=1)
    data = json.loads(result)
    assert isinstance(data, dict)
