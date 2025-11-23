import requests
from typing import Optional
import argparse

class Brewery:
    def __init__(self, name: str, brewery_type: Optional[str], city: Optional[str], state: Optional[str]):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.name} ({self.brewery_type}) - {self.city}, {self.state}"

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, help="Filtruj browary po mieście")
args = parser.parse_args()

params = {"per_page": 20}
if args.city:
    params["by_city"] = args.city

url = "https://api.openbrewerydb.org/v1/breweries"
data = requests.get(url, params=params).json()

breweries = [Brewery(item.get("name"), item.get("brewery_type"), item.get("city"), item.get("state")) for item in data]

for b in breweries:
    print(b)

