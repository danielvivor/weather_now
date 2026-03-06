import json # for reading API key from creds.json
import os # for checking if creds.json exists
from weather_api import get_weather

DATASET = "weather_history.json"

def load_dataset():
    if not os.path.exists(DATASET):
        return []
    with open(DATASET, "r") as f:
        return json.load(f)
    
    def save_dataset(data):
        with open(DATASET, "w") as f:
            json.dump(data, f, indent=4)


def add_entry(city):
    weather = get_weather(city)
    if weather is None:
        print("Error: Could not fetch weather (API key missing or invalid)")
        return

    entry = {
        "city": city,
        "temp_c": weather["main"]["temp"],
        "description": weather["weather"][0]["description"],
    }

    data = load_dataset()
    data.append(entry)
    save_dataset(data)

    print(f"Added weather for {city}")

    def list_entries():
        data = load_dataset()
    if not data:
        print("Dataset is empty")
        return

    for i, entry in enumerate(data, start=1):
        print(f"{i}. {entry['city']} — {entry['temp_c']}°C — {entry['description']}")

    def delete_entry(index):
        data = load_dataset()
        if index < 1 or index > len(data):
            print("Invalid index")
            return

        removed = data.pop(index - 1)
        save_dataset(data)
        print(f"Deleted entry for {removed['city']}")





