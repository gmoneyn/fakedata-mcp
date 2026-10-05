"""Generate realistic fake user profiles."""

import random
import string
from datetime import date, timedelta

FIRST_NAMES = {
    "en_US": ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth",
              "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Christopher", "Karen",
              "Daniel", "Lisa", "Matthew", "Nancy", "Anthony", "Betty", "Mark", "Margaret", "Donald", "Sandra",
              "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Quinn", "Harper", "Emerson"],
    "en_GB": ["Oliver", "Amelia", "George", "Isla", "Harry", "Ava", "Noah", "Mia", "Jack", "Isabella",
              "Leo", "Sophia", "Arthur", "Grace", "Muhammad", "Lily", "Oscar", "Freya", "Charlie", "Emily"],
    "de_DE": ["Lukas", "Anna", "Leon", "Marie", "Paul", "Sophie", "Felix", "Emilia", "Elias", "Mia",
              "Jonas", "Hannah", "Noah", "Lena", "Finn", "Lea", "Ben", "Clara", "Maximilian", "Johanna"],
    "ja_JP": ["Haruto", "Sakura", "Yuto", "Hina", "Sota", "Yui", "Riku", "Aoi", "Haruki", "Rio",
              "Minato", "Himari", "Kaito", "Mei", "Sora", "Mio", "Ren", "Kokona", "Asahi", "Rin"],
}

LAST_NAMES = {
    "en_US": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
              "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"],
    "en_GB": ["Smith", "Jones", "Williams", "Taylor", "Brown", "Davies", "Evans", "Wilson", "Thomas", "Roberts",
              "Johnson", "Lewis", "Walker", "Robinson", "Wood", "Thompson", "White", "Watson", "Jackson", "Wright"],
    "de_DE": ["Mueller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
              "Schaefer", "Koch", "Bauer", "Richter", "Klein", "Wolf", "Schroeder", "Neumann", "Schwarz", "Zimmermann"],
    "ja_JP": ["Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato",
              "Yoshida", "Yamada", "Sasaki", "Yamaguchi", "Matsumoto", "Inoue", "Kimura", "Hayashi", "Shimizu", "Yamazaki"],
}

DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "protonmail.com", "icloud.com", "fastmail.com", "mail.com"]

STREET_NAMES = ["Main St", "Oak Ave", "Maple Dr", "Cedar Ln", "Elm St", "Pine Rd", "Washington Blvd",
                "Park Ave", "Lake Dr", "Hill Rd", "River Rd", "Forest Ln", "Sunset Blvd", "Broadway",
                "Spring St", "Valley Rd", "Church St", "Market St", "Academy Dr", "Highland Ave"]

US_STATES = [
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("CA", "California"), ("CO", "Colorado"),
    ("CT", "Connecticut"), ("FL", "Florida"), ("GA", "Georgia"), ("IL", "Illinois"), ("MA", "Massachusetts"),
    ("MI", "Michigan"), ("MN", "Minnesota"), ("NY", "New York"), ("NC", "North Carolina"), ("OH", "Ohio"),
    ("OR", "Oregon"), ("PA", "Pennsylvania"), ("TX", "Texas"), ("VA", "Virginia"), ("WA", "Washington"),
]

US_CITIES = ["Springfield", "Riverside", "Franklin", "Clinton", "Madison", "Georgetown", "Arlington",
             "Salem", "Bristol", "Fairview", "Oakland", "Burlington", "Manchester", "Milton", "Newport"]

AREA_CODES = ["212", "310", "415", "512", "617", "702", "773", "818", "917", "305", "404", "503", "206", "720", "614"]

ALL_FIELDS = {"name", "email", "phone", "address", "dob", "username"}


class GenerateUsers:
    """Generate realistic fake user profiles."""

    def execute(self, count: int = 5, locale: str = "en_US", fields: str = "") -> dict:
        count = max(1, min(count, 100))
        if locale not in FIRST_NAMES:
            locale = "en_US"

        requested = set(f.strip() for f in fields.split(",") if f.strip()) if fields else ALL_FIELDS

        users = []
        for _ in range(count):
            first = random.choice(FIRST_NAMES[locale])
            last = random.choice(LAST_NAMES[locale])
            user = {}

            if "name" in requested:
                user["first_name"] = first
                user["last_name"] = last
                user["full_name"] = f"{first} {last}"

            if "email" in requested:
                sep = random.choice([".", "_", ""])
                num = random.choice(["", str(random.randint(1, 99))])
                user["email"] = f"{first.lower()}{sep}{last.lower()}{num}@{random.choice(DOMAINS)}"

            if "phone" in requested:
                area = random.choice(AREA_CODES)
                user["phone"] = f"+1-{area}-{random.randint(200,999)}-{random.randint(1000,9999)}"

            if "address" in requested:
                state_code, state_name = random.choice(US_STATES)
                user["address"] = {
                    "street": f"{random.randint(100, 9999)} {random.choice(STREET_NAMES)}",
                    "city": random.choice(US_CITIES),
                    "state": state_code,
                    "zip": f"{random.randint(10000, 99999)}",
                }

            if "dob" in requested:
                start = date(1960, 1, 1)
                end = date(2005, 12, 31)
                days_between = (end - start).days
                user["date_of_birth"] = str(start + timedelta(days=random.randint(0, days_between)))

            if "username" in requested:
                suffix = random.randint(1, 9999)
                user["username"] = f"{first.lower()}{last.lower()[0]}{suffix}"

            users.append(user)

        return {"users": users, "count": len(users), "locale": locale}
