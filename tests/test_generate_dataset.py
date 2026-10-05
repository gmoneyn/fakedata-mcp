"""Test generate_dataset tool."""

import json

from fakedata_mcp.tools.generate_dataset import generate_dataset


def test_generate_dataset_returns_json():
    result = generate_dataset(columns="test", rows=1, format="test")
    data = json.loads(result)
    assert isinstance(data, dict)
