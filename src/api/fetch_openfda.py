"""
Purpose:
In this file, I connect to the openFDA Drug Event API, download the raw
drug event data, and save the original API response as a JSON file.
"""

import json
from pathlib import Path

import requests


# API endpoint
API_URL = "https://api.fda.gov/drug/event.json"

# Number of records to download
LIMIT = 10

# Location to save the raw API response
OUTPUT_FOLDER = Path("data/raw/api")


def fetch_drug_events():
    """
    Here I am downloading drug event data from the openFDA API
    and saving the raw response.
    """

    
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    response = requests.get(API_URL, params={"limit": LIMIT})

    response.raise_for_status()

    data = response.json()
    existing_files = list(OUTPUT_FOLDER.glob("page_*.json"))
    page_number = len(existing_files) + 1

    output_file = OUTPUT_FOLDER / f"page_{page_number:03d}.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Downloaded {LIMIT} records.")
    print(f"Saved data to: {output_file}")

if __name__ == "__main__":
    fetch_drug_events()