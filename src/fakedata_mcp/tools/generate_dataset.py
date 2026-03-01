"""Generate a custom dataset with user-defined columns and types. Supports: string, integer, float, boolean, email, name, phone, date, url, uuid, ip_address, color, company, job_title."""

import json

from fakedata_mcp.services.generate_dataset_service import GenerateDataset


def generate_dataset(columns: str, rows: int = 10, format: str = "json") -> str:
    """Generate a custom dataset with user-defined columns and types. Supports: string, integer, float, boolean, email, name, phone, date, url, uuid, ip_address, color, company, job_title

    Returns:
        Dataset in requested format
    """
    service = GenerateDataset()
    result = service.execute(columns=columns, rows=rows, format=format)
    return json.dumps(result, indent=2)
