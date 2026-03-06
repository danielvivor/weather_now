import json
import requests
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_api_key():
    try:
        config_path = resource_path("creds.json")
        with open(config_path, "r") as f:
            config = json.load(f)
            return config["api"]["key"]
    except:
        return None

def get_weather(city):
    api_key = load_api_key()
    if not api_key:
        return None

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except:
        return None