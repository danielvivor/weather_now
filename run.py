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
    while True:
        print("\n--- Weather CLI ---")
        print("1. Add weather entry")
        print("2. List entries")
        print("3. Delete entry")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): \n")
        
        if choice == '1':
            city = input("Enter city name: \n")
            add_entry(city)
        elif choice == '2':
            list_entries()
        elif choice == '3':
            index = int(input("Enter index to delete: \n"))
            delete_entry(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
