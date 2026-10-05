"""Generate fake street addresses."""

import random

STREET_NAMES_US = ["Main St", "Oak Ave", "Maple Dr", "Cedar Ln", "Elm St", "Pine Rd", "Washington Blvd",
                   "Park Ave", "Lake Dr", "Hill Rd", "River Rd", "Forest Ln", "Sunset Blvd", "Broadway",
                   "Spring St", "Valley Rd", "Church St", "Market St", "Highland Ave", "Union St"]

COUNTRY_DATA = {
    "US": {
        "cities": [
            ("New York", "NY", 40.7128, -74.0060), ("Los Angeles", "CA", 34.0522, -118.2437),
            ("Chicago", "IL", 41.8781, -87.6298), ("Houston", "TX", 29.7604, -95.3698),
            ("Phoenix", "AZ", 33.4484, -112.0740), ("Philadelphia", "PA", 39.9526, -75.1652),
            ("San Antonio", "TX", 29.4241, -98.4936), ("San Diego", "CA", 32.7157, -117.1611),
            ("Dallas", "TX", 32.7767, -96.7970), ("Austin", "TX", 30.2672, -97.7431),
            ("Denver", "CO", 39.7392, -104.9903), ("Seattle", "WA", 47.6062, -122.3321),
            ("Portland", "OR", 45.5152, -122.6784), ("Miami", "FL", 25.7617, -80.1918),
            ("Atlanta", "GA", 33.7490, -84.3880), ("Boston", "MA", 42.3601, -71.0589),
        ],
        "zip_format": lambda: f"{random.randint(10000, 99999)}",
        "streets": STREET_NAMES_US,
        "country_name": "United States",
    },
    "GB": {
        "cities": [
            ("London", "England", 51.5074, -0.1278), ("Manchester", "England", 53.4808, -2.2426),
            ("Birmingham", "England", 52.4862, -1.8904), ("Edinburgh", "Scotland", 55.9533, -3.1883),
            ("Glasgow", "Scotland", 55.8642, -4.2518), ("Liverpool", "England", 53.4084, -2.9916),
            ("Bristol", "England", 51.4545, -2.5879), ("Leeds", "England", 53.8008, -1.5491),
        ],
        "zip_format": lambda: f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))}{random.randint(1,9)} {random.randint(1,9)}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))}",
        "streets": ["High St", "Church Rd", "Station Rd", "Victoria Rd", "Park Rd", "London Rd", "Kings Rd", "Queen St", "Mill Ln", "Green Ln"],
        "country_name": "United Kingdom",
    },
    "DE": {
        "cities": [
            ("Berlin", "Berlin", 52.5200, 13.4050), ("Munich", "Bavaria", 48.1351, 11.5820),
            ("Hamburg", "Hamburg", 53.5511, 9.9937), ("Frankfurt", "Hesse", 50.1109, 8.6821),
            ("Cologne", "North Rhine-Westphalia", 50.9375, 6.9603), ("Stuttgart", "Baden-Wuerttemberg", 48.7758, 9.1829),
        ],
        "zip_format": lambda: f"{random.randint(10000, 99999)}",
        "streets": ["Hauptstrasse", "Berliner Strasse", "Bahnhofstrasse", "Gartenstrasse", "Schulstrasse", "Dorfstrasse", "Kirchstrasse", "Waldstrasse"],
        "country_name": "Germany",
    },
    "CA": {
        "cities": [
            ("Toronto", "ON", 43.6532, -79.3832), ("Vancouver", "BC", 49.2827, -123.1207),
            ("Montreal", "QC", 45.5017, -73.5673), ("Calgary", "AB", 51.0447, -114.0719),
            ("Ottawa", "ON", 45.4215, -75.6972), ("Edmonton", "AB", 53.5461, -113.4938),
        ],
        "zip_format": lambda: f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))}{random.randint(1,9)}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))} {random.randint(1,9)}{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))}{random.randint(1,9)}",
        "streets": ["King St", "Queen St", "Yonge St", "Bay St", "Bloor St", "Dundas St", "College St", "Maple Ave"],
        "country_name": "Canada",
    },
    "AU": {
        "cities": [
            ("Sydney", "NSW", -33.8688, 151.2093), ("Melbourne", "VIC", -37.8136, 144.9631),
            ("Brisbane", "QLD", -27.4698, 153.0251), ("Perth", "WA", -31.9505, 115.8605),
            ("Adelaide", "SA", -34.9285, 138.6007), ("Canberra", "ACT", -35.2809, 149.1300),
        ],
        "zip_format": lambda: f"{random.randint(2000, 7999)}",
        "streets": ["George St", "King St", "Elizabeth St", "Collins St", "Bourke St", "Flinders St", "Pitt St", "Market St"],
        "country_name": "Australia",
    },
}


class GenerateAddresses:
    """Generate fake street addresses."""

    def execute(self, count: int = 5, country: str = "US") -> dict:
        count = max(1, min(count, 100))
        if country not in COUNTRY_DATA:
            country = "US"

        data = COUNTRY_DATA[country]
        addresses = []

        for _ in range(count):
            city, state, lat, lon = random.choice(data["cities"])
            lat_offset = random.uniform(-0.05, 0.05)
            lon_offset = random.uniform(-0.05, 0.05)

            addresses.append({
                "street": f"{random.randint(1, 9999)} {random.choice(data['streets'])}",
                "city": city,
                "state": state,
                "zip": data["zip_format"](),
                "country": country,
                "country_name": data["country_name"],
                "coordinates": {
                    "latitude": round(lat + lat_offset, 6),
                    "longitude": round(lon + lon_offset, 6),
                },
            })

        return {"addresses": addresses, "count": len(addresses), "country": country}
