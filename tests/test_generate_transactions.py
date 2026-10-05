"""Test generate_transactions tool."""

import json

from fakedata_mcp.tools.generate_transactions import generate_transactions


def test_generate_transactions_returns_json():
    result = generate_transactions(count=1, min_amount=1.0, max_amount=1.0, currency="test")
    data = json.loads(result)
    assert isinstance(data, dict)
