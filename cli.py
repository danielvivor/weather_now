import json # for reading API key from creds.json
import os # for checking if creds.json exists
from weather_api import get_weather

DATASET = "weather_history.json"

def load_dataset():
    if not os.path.exists(DATASET):
        return []
    with open(DATASET, "r") as f:
        return json.load(f)


