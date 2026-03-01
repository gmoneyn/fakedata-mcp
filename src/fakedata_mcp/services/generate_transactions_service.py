"""Generate fake financial transactions."""

import random
from datetime import datetime, timedelta

MERCHANTS_BY_CATEGORY = {
    "groceries": ["Whole Foods", "Trader Joe's", "Kroger", "Safeway", "Costco", "Aldi", "Publix", "Wegmans"],
    "dining": ["Chipotle", "Starbucks", "Olive Garden", "Panera Bread", "Five Guys", "Sweetgreen", "Shake Shack", "Chick-fil-A"],
    "transport": ["Uber", "Lyft", "Shell Gas", "Chevron", "BP", "Delta Airlines", "United Airlines", "Amtrak"],
    "shopping": ["Amazon", "Target", "Walmart", "Best Buy", "Nike", "Apple Store", "Home Depot", "Nordstrom"],
    "entertainment": ["Netflix", "Spotify", "AMC Theatres", "Steam", "PlayStation Store", "Ticketmaster", "Audible", "Disney+"],
    "utilities": ["AT&T", "Verizon", "Comcast", "ConEdison", "National Grid", "T-Mobile", "Spectrum", "PG&E"],
    "health": ["CVS Pharmacy", "Walgreens", "Kaiser Permanente", "UnitedHealth", "Rite Aid", "GoodRx", "Peloton", "Planet Fitness"],
    "subscriptions": ["Adobe", "Microsoft 365", "Dropbox", "Notion", "Slack", "Zoom", "GitHub", "Figma"],
}

PAYMENT_METHODS = ["credit_card", "debit_card", "bank_transfer", "apple_pay", "google_pay", "paypal"]
STATUSES = ["completed", "completed", "completed", "completed", "pending", "refunded"]  # weighted toward completed

CURRENCY_SYMBOLS = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3", "JPY": "\u00a5"}


class GenerateTransactions:
    """Generate fake financial transactions."""

    def execute(self, count: int = 10, min_amount: float = 1.0, max_amount: float = 1000.0, currency: str = "USD") -> dict:
        count = max(1, min(count, 500))
        min_amount = max(0.01, min_amount)
        max_amount = max(min_amount + 0.01, max_amount)
        if currency not in CURRENCY_SYMBOLS:
            currency = "USD"
        symbol = CURRENCY_SYMBOLS[currency]

        now = datetime.now()
        transactions = []

        for _ in range(count):
            category = random.choice(list(MERCHANTS_BY_CATEGORY.keys()))
            merchant = random.choice(MERCHANTS_BY_CATEGORY[category])
            amount = round(random.uniform(min_amount, max_amount), 2)
            days_ago = random.randint(0, 90)
            tx_date = now - timedelta(days=days_ago, hours=random.randint(0, 23), minutes=random.randint(0, 59))
            status = random.choice(STATUSES)

            transactions.append({
                "id": f"txn_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=12))}",
                "amount": amount,
                "amount_formatted": f"{symbol}{amount:,.2f}",
                "currency": currency,
                "merchant": merchant,
                "category": category,
                "payment_method": random.choice(PAYMENT_METHODS),
                "status": status,
                "date": tx_date.strftime("%Y-%m-%d"),
                "timestamp": tx_date.isoformat(),
            })

        transactions.sort(key=lambda t: t["timestamp"], reverse=True)
        total = round(sum(t["amount"] for t in transactions if t["status"] == "completed"), 2)

        return {
            "transactions": transactions,
            "count": len(transactions),
            "total_completed": total,
            "total_formatted": f"{symbol}{total:,.2f}",
            "currency": currency,
        }
