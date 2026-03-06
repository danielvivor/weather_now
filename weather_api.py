import json
import requests
import os
import sys


def resource_path(relative_path):
    """Return absolute path to resource (supports PyInstaller)."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def load_api_key():
    """Load API key from creds.json."""
    try:
        config_path = resource_path("creds.json")
        with open(config_path, "r") as f:
            config = json.load(f)
            return config["api"]["key"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return None


def get_weather(city):
    """Fetch weather data for a given city."""
    api_key = load_api_key()
    if not api_key:
        return None

    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None