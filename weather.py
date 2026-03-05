# Import required modules
import sys  # handles systems variables for python interpreter

import requests  # allows us to send HTTP requests

import json  # read API key from creds.json file

from PyQt5.QtWidgets import (
    QApplication,  # main application class for PyQt5
    QWidget,  # base class for all UI objects in PyQt5
    QVBoxLayout,  # vertical layout manager
    QPushButton,  # button widget
    QLabel,  # label widget
    QLineEdit,  # single-line text input widget
)

from PyQt5.QtCore import (
    Qt,
)  # used for alignment and other core functionalities in PyQt5


# Create the main application class
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        self.error_label = QLabel("")  # dedicated error label

        self.temperature_label = QLabel("70 °C", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

        self.initUI()

 # Build the layout and connect events
    def initUI(self):
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

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.error_label.setObjectName("error_label")

        try:
            with open("styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Warning: styles.qss not found. Using default styling.")

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    # Fetch weather data from the API
    def get_weather(self):

        # Read API key from config.json
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
                api_key = config["api"]["key"]
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            api_key = None

        if not api_key:
            self.display_error("API key missing.\nAdd it to config.json under api → key.")
            return
        
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name.")
            return
        
        self.get_weather_button.setText("Loading...")
        self.get_weather_button.setEnabled(False)

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={api_key}&units=metric"
        )

        try:
            response = requests.get(url, timeout=5)
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




# Start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
