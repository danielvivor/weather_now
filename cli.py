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



