import requests
from typing import Optional


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: Optional[str],
        street: Optional[str],
        city: Optional[str],
        state: Optional[str],
        postal_code: Optional[str],
        country: Optional[str],
        longitude: Optional[str],
        latitude: Optional[str],
        phone: Optional[str],
        website_url: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return f"{self.name} ({self.brewery_type}) - {self.city}, {self.state}"


url = "https://api.openbrewerydb.org/v1/breweries"
params = {"per_page": 20}
response = requests.get(url, params=params)
data = response.json()

breweries = []
for item in data:
    brewery = Brewery(
        id=item.get("id"),
        name=item.get("name"),
        brewery_type=item.get("brewery_type"),
        street=item.get("street"),
        city=item.get("city"),
        state=item.get("state"),
        postal_code=item.get("postal_code"),
        country=item.get("country"),
        longitude=item.get("longitude"),
        latitude=item.get("latitude"),
        phone=item.get("phone"),
        website_url=item.get("website_url")
    )
    breweries.append(brewery)

for b in breweries:
    print(b)
