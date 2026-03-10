from flask import Flask, jsonify
from weather_api import get_weather

app = Flask(__name__)

@app.get("/weather/<city>")
def weather(city):
    """Return weather data for a given city as JSON."""
    data = get_weather(city)
    if data is None:
        return jsonify({"error": "Could not fetch weather"}), 400
    return jsonify(data)

@app.get("/")
def home():
    """Health check endpoint."""
    return jsonify({"status": "ok", "message": "Weather API is running"})