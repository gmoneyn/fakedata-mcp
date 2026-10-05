"""Generate fake company profiles."""

import random
from datetime import date

PREFIXES = ["Global", "Advanced", "Prime", "Summit", "Apex", "Nexus", "Vertex", "Quantum", "Atlas", "Zenith",
            "Vanguard", "Pinnacle", "Crest", "Core", "Nova", "Pulse", "Swift", "Bright", "True", "Clear"]

SUFFIXES_BY_INDUSTRY = {
    "tech": ["Systems", "Technologies", "Software", "Digital", "Labs", "AI", "Cloud", "Data", "Networks", "Solutions"],
    "finance": ["Capital", "Financial", "Advisors", "Partners", "Investments", "Holdings", "Wealth", "Group", "Banking", "Fund"],
    "healthcare": ["Health", "Medical", "Therapeutics", "Pharma", "BioSciences", "Care", "Wellness", "Diagnostics", "Life Sciences", "Genomics"],
    "retail": ["Brands", "Commerce", "Goods", "Market", "Retail", "Store", "Supply", "Trading", "Outlet", "Provisions"],
    "manufacturing": ["Industries", "Manufacturing", "Engineering", "Materials", "Fabrication", "Works", "Production", "Dynamics", "Forge", "Assembly"],
}

ALL_INDUSTRIES = list(SUFFIXES_BY_INDUSTRY.keys())

TLDS = [".com", ".io", ".co", ".net", ".tech", ".ai"]


class GenerateCompanies:
    """Generate fake company profiles."""

    def execute(self, count: int = 5, industry: str = "") -> dict:
        count = max(1, min(count, 100))
        industries = [industry] if industry in SUFFIXES_BY_INDUSTRY else ALL_INDUSTRIES

        companies = []
        for _ in range(count):
            ind = random.choice(industries)
            prefix = random.choice(PREFIXES)
            suffix = random.choice(SUFFIXES_BY_INDUSTRY[ind])
            name = f"{prefix} {suffix}"

            founded = random.randint(1985, 2024)
            age = 2026 - founded
            base_revenue = random.uniform(500_000, 50_000_000)
            growth_factor = 1 + (age * 0.05)
            revenue = round(base_revenue * growth_factor, 2)
            employees = max(5, int(revenue / random.uniform(80_000, 200_000)))

            slug = name.lower().replace(" ", "")
            website = f"https://www.{slug}{random.choice(TLDS)}"

            companies.append({
                "name": name,
                "industry": ind,
                "founded": founded,
                "revenue": revenue,
                "revenue_formatted": f"${revenue:,.2f}",
                "employee_count": employees,
                "website": website,
            })

        return {"companies": companies, "count": len(companies)}
