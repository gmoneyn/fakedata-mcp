"""Generate fake street addresses with street, city, state, zip, country, and coordinates."""

import json

from fakedata_mcp.services.generate_addresses_service import GenerateAddresses


def generate_addresses(count: int = 5, country: str = "US") -> str:
    """Generate fake street addresses with street, city, state, zip, country, and coordinates

    Returns:
        JSON array of address objects
    """
    service = GenerateAddresses()
    result = service.execute(count=count, country=country)
    return json.dumps(result, indent=2)
