# notion_google_places_sync.py
# Version History:
# 1.0.0 (2024-12-01) - Initial release integrating Google Places API with Notion API.

import os
import requests
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set your API keys from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")

# Initialize the Notion client
notion = Client(auth=NOTION_API_KEY)

def search_places(query, location, radius=5000):
    """Fetch data from Google Places API."""
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": location,
        "radius": radius,
        "key": GOOGLE_API_KEY,
        "region": "ca",  # Restrict search to Canada
    }
    response = requests.get(url, params=params)
    return response.json()

def get_place_details(place_id):
    """Fetch detailed information for a place."""
    url = f"https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,rating,user_ratings_total,formatted_address,formatted_phone_number,website",
        "key": GOOGLE_API_KEY,
    }
    response = requests.get(url, params=params)
    return response.json()

def add_to_notion(data):
    """Add a business to Notion."""
    properties = {
        "Company": {"title": [{"text": {"content": data["name"]}}]},
        "Google Rating": {"number": data.get("rating", 0)},
        "Review Count": {"number": data.get("user_ratings_total", 0)},
        "Location": {"rich_text": [{"text": {"content": data.get("formatted_address", "")}}]},
        "Phone Number": {"phone_number": data.get("formatted_phone_number", None)},  # Corrected type
        "Website": {"url": data.get("website", None)},
    }
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties=properties)

# Example Usage
def main():
    # Replace with desired search parameters
    query = "trailer rentals"  # Adjust the query as needed
    location = "45.500260452766184, -73.56513584465054"  # Montreal, Quebec coordinates
    radius = 5000  # Radius in meters

    # Search for places
    results = search_places(query, location, radius)

    # Process each result
    for place in results.get("results", []):
        place_id = place.get("place_id")
        if place_id:
            details = get_place_details(place_id)
            if details.get("result"):
                add_to_notion(details["result"])

if __name__ == "__main__":
    main()
