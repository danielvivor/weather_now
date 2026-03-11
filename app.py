from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

@app.route("/")
def home():
    return jsonify({"status": "Weather API running"}), 200

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing 'city' parameter"}), 400

    try:
        data = fetch_weather(city)
        return jsonify(data), 200
    except requests.exceptions.HTTPError:
        return jsonify({"error": "City not found"}), 404
    except Exception:
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)