"""Generate fake financial transactions with amount, date, merchant, category, payment method, and status."""

import json

from fakedata_mcp.services.generate_transactions_service import GenerateTransactions


def generate_transactions(count: int = 10, min_amount: float = 1.0, max_amount: float = 1000.0, currency: str = "USD") -> str:
    """Generate fake financial transactions with amount, date, merchant, category, payment method, and status

    Returns:
        JSON array of transaction objects
    """
    service = GenerateTransactions()
    result = service.execute(count=count, min_amount=min_amount, max_amount=max_amount, currency=currency)
    return json.dumps(result, indent=2)
