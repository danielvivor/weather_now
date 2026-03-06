import json
import os
from weather_api import get_weather

DATASET = "weather_history.json"


def load_dataset():
    """Load dataset from JSON file."""
    if not os.path.exists(DATASET):
        return []
    with open(DATASET, "r") as f:
        return json.load(f)


def save_dataset(data):
    """Save dataset to JSON file."""
    with open(DATASET, "w") as f:
        json.dump(data, f, indent=4)


def add_entry(city):
    """Add a new weather entry for a city."""
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
    """List all saved weather entries."""
    data = load_dataset()
    if not data:
        print("Dataset is empty")
        return

    for i, entry in enumerate(data, start=1):
        print(
            f"{i}. {entry['city']} — " f"{entry['temp_c']}°C — {entry['description']}"
        )


def delete_entry(index):
    """Delete an entry by index."""
    data = load_dataset()

    if index < 1 or index > len(data):
        print("Invalid index")
        return

    removed = data.pop(index - 1)
    save_dataset(data)
    print(f"Deleted entry for {removed['city']}")


def run_cli():
    """Run the interactive CLI loop."""
    print("Weather CLI Mode")
    print("Commands: add <city>, list, delete <index>, exit")

    while True:
        cmd = input("> ").strip().split()

        if not cmd:
            continue

        if cmd[0] == "add" and len(cmd) > 1:
            add_entry(" ".join(cmd[1:]))

        elif cmd[0] == "list":
            list_entries()

        elif cmd[0] == "delete" and len(cmd) > 1:
            try:
                delete_entry(int(cmd[1]))
            except ValueError:
                print("Invalid index")

        elif cmd[0] == "exit":
            break

        else:
            print("Unknown command")
