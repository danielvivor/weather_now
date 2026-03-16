import os
import requests

def load_api_key():
    return os.environ.get("API_KEY")

def get_weather(city):
    api_key = load_api_key()
    if not api_key:
        return {"error": "API key missing"}

    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
