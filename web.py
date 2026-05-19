from flask import Flask, request, jsonify
from weather_api import get_weather # Import your existing engine

app = Flask(__name__)

@app.route("/")
def index():
    return "Weather API is running! Use /weather?city=Munich to get data."

@app.route("/weather")
def weather():
    city = request.args.get('city', 'Munich') # Get city from URL
    data = get_weather(city) # Call your scientific engine
    return jsonify(data) # Return the data as JSON for your React frontend

if __name__ == "__main__":
    app.run()