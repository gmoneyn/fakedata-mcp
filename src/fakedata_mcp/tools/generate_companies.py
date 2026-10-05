"""Generate fake company profiles with name, industry, revenue, employee count, founded date, and website."""

import json

from fakedata_mcp.services.generate_companies_service import GenerateCompanies


def generate_companies(count: int = 5, industry: str = "") -> str:
    """Generate fake company profiles with name, industry, revenue, employee count, founded date, and website

    Returns:
        JSON array of company objects
    """
    service = GenerateCompanies()
    result = service.execute(count=count, industry=industry)
    return json.dumps(result, indent=2)
