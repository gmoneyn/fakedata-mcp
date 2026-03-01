"""Generate realistic fake user profiles with name, email, phone, address, date of birth, and username."""

import json

from fakedata_mcp.services.generate_users_service import GenerateUsers


def generate_users(count: int = 5, locale: str = "en_US", fields: str = "") -> str:
    """Generate realistic fake user profiles with name, email, phone, address, date of birth, and username

    Returns:
        JSON array of user objects
    """
    service = GenerateUsers()
    result = service.execute(count=count, locale=locale, fields=fields)
    return json.dumps(result, indent=2)
