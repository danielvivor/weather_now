import argparse
import json
import os
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

    if "error" in weather:
        print("Error:", weather["error"])
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

def main():
    parser = argparse.ArgumentParser(description="Weather CLI")
    parser.add_argument("--add", type=str, help="Add weather entry for a city")
    parser.add_argument("--list", action="store_true", help="List all entries")
    parser.add_argument("--delete", type=int, help="Delete entry by index")

    args = parser.parse_args()

    if args.add:
        add_entry(args.add)
    elif args.list:
        list_entries()
    elif args.delete:
        delete_entry(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()