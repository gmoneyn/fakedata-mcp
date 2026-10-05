"""Generate custom datasets with user-defined schemas."""

import csv
import io
import json
import random
import string
import uuid
from datetime import date, timedelta

FIRST_NAMES = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth",
               "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Sarah", "Daniel", "Emma", "Noah"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Anderson"]
COMPANIES = ["Acme Corp", "TechVault", "DataPrime", "CloudNova", "PixelForge", "NexGen", "ZenithAI", "CoreStack",
             "BrightPath", "SwiftLogic", "PulseData", "QuantumEdge", "AtlasWorks", "SummitLabs", "ApexSoft"]
JOB_TITLES = ["Software Engineer", "Product Manager", "Data Analyst", "Designer", "Marketing Manager",
              "Sales Representative", "DevOps Engineer", "QA Engineer", "CTO", "CEO", "VP of Engineering",
              "Account Executive", "Customer Success Manager", "Solutions Architect", "Technical Writer"]
COLORS = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8", "#F7DC6F",
          "#BB8FCE", "#85C1E9", "#F0B27A", "#82E0AA", "#F1948A", "#AED6F1", "#D7BDE2", "#A3E4D7"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "company.com", "example.com", "test.io"]

TYPE_GENERATORS = {
    "string": lambda: "".join(random.choices(string.ascii_lowercase, k=random.randint(5, 12))),
    "integer": lambda: random.randint(1, 10000),
    "float": lambda: round(random.uniform(0.0, 10000.0), 2),
    "boolean": lambda: random.choice([True, False]),
    "email": lambda: f"{random.choice(FIRST_NAMES).lower()}.{random.choice(LAST_NAMES).lower()}{random.randint(1,99)}@{random.choice(DOMAINS)}",
    "name": lambda: f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
    "phone": lambda: f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}",
    "date": lambda: str(date(2020, 1, 1) + timedelta(days=random.randint(0, 2000))),
    "url": lambda: f"https://www.{''.join(random.choices(string.ascii_lowercase, k=8))}.com/{'/'.join(random.choices(string.ascii_lowercase, k=random.randint(1, 3)))}",
    "uuid": lambda: str(uuid.uuid4()),
    "ip_address": lambda: f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
    "color": lambda: random.choice(COLORS),
    "company": lambda: random.choice(COMPANIES),
    "job_title": lambda: random.choice(JOB_TITLES),
}

SUPPORTED_TYPES = list(TYPE_GENERATORS.keys())


class GenerateDataset:
    """Generate custom datasets with user-defined columns and types."""

    def execute(self, columns: str, rows: int = 10, format: str = "json") -> dict:
        rows = max(1, min(rows, 1000))

        try:
            col_spec = json.loads(columns)
        except (json.JSONDecodeError, TypeError):
            return {"error": f"Invalid columns JSON. Expected format: {{\"name\": \"name\", \"score\": \"integer\"}}. Supported types: {', '.join(SUPPORTED_TYPES)}"}

        if not isinstance(col_spec, dict):
            return {"error": "columns must be a JSON object mapping column names to types"}

        for col_name, col_type in col_spec.items():
            if col_type not in TYPE_GENERATORS:
                return {"error": f"Unknown type '{col_type}' for column '{col_name}'. Supported: {', '.join(SUPPORTED_TYPES)}"}

        data = []
        for _ in range(rows):
            row = {}
            for col_name, col_type in col_spec.items():
                row[col_name] = TYPE_GENERATORS[col_type]()
            data.append(row)

        if format == "csv":
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=list(col_spec.keys()))
            writer.writeheader()
            writer.writerows(data)
            result = output.getvalue()
            return {"data": result, "format": "csv", "rows": rows, "columns": list(col_spec.keys())}

        return {"data": data, "format": "json", "rows": rows, "columns": list(col_spec.keys())}
