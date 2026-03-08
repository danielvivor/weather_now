"""
Weather Now — PyQt5 GUI application for fetching live weather data.
Includes optional CLI mode via --cli flag.
"""

# Import required modules
import sys  # handles system variables for Python interpreter
import requests  # allows us to send HTTP requests
import json  # read API key from creds.json file
import argparse  # for command-line argument parsing
import time  # used for artificial delay simulation

# PyQt5 imports:
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)
from PyQt5.QtCore import Qt


# -------------------------------------------------------------------
# Slow network simulation wrapper
# -------------------------------------------------------------------
def slow_request(url, delay=3, timeout=5):
    """Simulate slow network by waiting before making the request."""
    time.sleep(delay)  # artificial delay for testing
    return requests.get(url, timeout=timeout)


# Create the main application class
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        self.error_label = QLabel("")  # dedicated error label

        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.init_ui()

    # Build the layout and connect events
    def init_ui(self):
        self.setWindowTitle("Weather Now")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.error_label)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        # Center alignment for all labels
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Object names for QSS styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.error_label.setObjectName("error_label")

        # Load stylesheet
        try:
            with open("styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Warning: styles.qss not found. Using default styling.")

        # Connect button + Enter key
        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    # Fetch weather data from the API
    def get_weather(self):
        # Read API key from creds.json
        try:
            with open("creds.json", "r") as f:
                creds = json.load(f)
                api_key = creds["api"]["key"]
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            api_key = None

        if not api_key:
            self.display_error(
                "API key missing.\nAdd it to creds.json under api → key."
            )
            return

        city = self.city_input.text().strip()
        if not city:
            self.display_error("Please enter a city name.")
            return

        self.get_weather_button.setText("Loading...")
        self.get_weather_button.setEnabled(False)

        url = (
            "https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={api_key}&units=metric"
        )

        try:
            # ---------------------------------------------------------
            # Replace direct API call with slow_request() for testing
            # ---------------------------------------------------------
            response = slow_request(url, delay=0, timeout=0.001)
            # ---------------------------------------------------------

            response.raise_for_status()
            data = response.json()

            if str(data.get("cod")) == "200":
                self.display_weather(data)
            else:
                self.display_error(data.get("message", "Unknown error"))

        except requests.exceptions.HTTPError as http_error:
            status = http_error.response.status_code

            match status:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Server error:\nTry again later")
                case 502:
                    self.display_error("Bad gateway:\nServer error")
                case 503:
                    self.display_error("Service unavailable:\nServer down")
                case 504:
                    self.display_error("Gateway timeout:\nServer not responding")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

        finally:
            self.get_weather_button.setText("Get Weather")
            self.get_weather_button.setEnabled(True)

    # Display error messages in the GUI
    def display_error(self, message):
        self.error_label.setText(message)
        self.temperature_label.clear()
        self.emoji_label.clear()
        self.description_label.clear()

    # Display weather information in the GUI
    def display_weather(self, data):
        self.error_label.clear()

        temp_c = data["main"]["temp"]
        temp_f = temp_c * 9 / 5 + 32

        main = data["weather"][0]["main"]
        description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temp_c:.0f}°C | {temp_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(main))
        self.description_label.setText(description)

    # Convert weather "main" → emoji
    @staticmethod
    def get_weather_emoji(main):
        emoji_map = {
            "Thunderstorm": "⛈️",
            "Drizzle": "🌦️",
            "Rain": "☔",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Smoke": "🌫️",
            "Haze": "🌫️",
            "Dust": "🌫️",
            "Fog": "🌫️",
            "Squall": "🌬️",
            "Tornado": "🌪️",
            "Clear": "☀️",
            "Clouds": "☁️",
        }
        return emoji_map.get(main, "")


# Start the application
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather App with GUI and CLI modes")
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in command-line mode",
    )
    args = parser.parse_args()

    if args.cli:
        from cli import run_cli
        run_cli()
    else:
        app = QApplication(sys.argv)
        weather_app = WeatherApp()
        weather_app.show()
        sys.exit(app.exec_())