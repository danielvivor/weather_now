"""
Weather Now — PyQt5 GUI application for fetching live weather data.
Includes optional CLI mode via --cli flag.
"""

# Import required modules
import sys  # handles system variables for Python interpreter
import requests  # allows us to send HTTP requests
import json  # read API key from creds.json file
import argparse  # for command-line argument parsing
import re  # for validating city names with regex


# CLI MODE (Codespaces)
def run_cli():
    """
    Interactive CLI mode.
    Commands:
      add <city>      Fetches weather for a city and saves it
      list            Displays all saved weather entries
      delete <index>  Removes an entry by its list number
      exit            Exits the CLI mode
    """

    # Read API key from creds.json
    try:
        with open("creds.json", "r") as f:
            creds = json.load(f)
            api_key = creds["api"]["key"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        print("API key missing. Add it to creds.json under api → key.")
        return

    saved_entries = []  # store weather results

    print("\nWeather Now CLI Mode")
    print("Type 'help' to see available commands.\n")

    while True:
        command = input("> ").strip()

        # exit
        if command == "exit":
            print("Exiting CLI mode.")
            break

        # help
        elif command == "help":
            print("""
Commands:
  add <city>      Fetches weather for a city and saves it
  list            Displays all saved weather entries
  delete <index>  Removes an entry by its list number
  exit            Exits the CLI mode
""")

        # list
        elif command == "list":
            if not saved_entries:
                print("No saved entries.")
            else:
                print("\nSaved Weather Entries:")
                for i, entry in enumerate(saved_entries, start=1):
                    print(f"{i}. {entry}")
                print()

        # delete <index>
        elif command.startswith("delete "):
            try:
                index = int(command.split()[1]) - 1
                removed = saved_entries.pop(index)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid index.")

        # add <city>
        elif command.startswith("add "):
            city = command[4:].strip()

            # Regex validation for city names (allows letters, spaces, and hyphens)
            if not re.match(r"^[a-zA-Z\s-]+$", city):
                print("Invalid city name. Please use only letters, spaces, and hyphens.")
                continue

            url = (
                "https://api.openweathermap.org/data/2.5/weather?"
                f"q={city}&appid={api_key}&units=metric"
            )

            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                data = response.json()

                if str(data.get("cod")) != "200":
                    print("Error:", data.get("message", "Unknown error"))
                    continue

                temp_c = data["main"]["temp"]
                temp_f = temp_c * 9 / 5 + 32
                description = data["weather"][0]["description"].capitalize()

                entry = f"{city}: {temp_c:.0f}°C | {temp_f:.0f}°F — {description}"
                saved_entries.append(entry)

                print("Saved:", entry)

            except Exception as e:
                print("Error:", e)

        # unknown command
        else:
            print("Unknown command. Type 'help' for a list of commands.")


# MAIN ENTRY POINT
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Weather App with GUI and CLI modes"
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in command-line mode",
    )
    args = parser.parse_args()

    # CLI MODE
    if args.cli:
        run_cli()

   
    # GUI MODE
    else:
        # PyQt5 imports:
        # QApplication — main application class for PyQt5
        # QWidget — base class for all UI objects in PyQt5
        # QVBoxLayout — vertical layout manager
        # QPushButton — button widget
        # QLabel — label widget
        # QLineEdit — single-line text input widget
        from PyQt5.QtWidgets import (
            QApplication,
            QWidget,
            QVBoxLayout,
            QPushButton,
            QLabel,
            QLineEdit,
        )

        # Qt core utilities (alignment, flags, etc.)
        from PyQt5.QtCore import Qt

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

                # Regex validation for city names (allows letters, spaces, and hyphens)
                if not re.match(r"^[a-zA-Z\s-]+$", city):
                    self.display_error(
                        "Invalid city name.\nPlease use only letters, spaces, and hyphens."
                    )
                    return

                self.get_weather_button.setText("Loading...")
                self.get_weather_button.setEnabled(False)

                url = (
                    "https://api.openweathermap.org/data/2.5/weather?"
                    f"q={city}&appid={api_key}&units=metric"
                )

                try:
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    data = response.json()

                    if str(data.get("cod")) == "200":
                        self.display_weather(data)
                    else:
                        self.display_error(
                            data.get("message", "Unknown error"))

                except requests.exceptions.HTTPError as http_error:
                    status = http_error.response.status_code

                    # Match HTTP status codes to messages
                    match status:
                        case 400:
                            self.display_error(
                                "Bad request:\nPlease check your input")
                        case 401:
                            self.display_error(
                                "Unauthorized:\nInvalid API key")
                        case 403:
                            self.display_error("Forbidden:\nAccess denied")
                        case 404:
                            self.display_error("Not Found:\nCity not found")
                        case 429:
                            self.display_error(
                                "Rate limit exceeded:\nPlease wait and try again"
                            )
                        case 500:
                            self.display_error(
                                "Server error:\nTry again later")
                        case 502:
                            self.display_error("Bad gateway:\nServer error")
                        case 503:
                            self.display_error(
                                "Service unavailable:\nServer down")
                        case 504:
                            self.display_error(
                                "Gateway timeout:\nServer not responding"
                            )
                        case _:
                            self.display_error(
                                f"HTTP error occurred:\n{http_error}")

                except requests.exceptions.ConnectionError:
                    self.display_error(
                        "Connection Error:\nCheck your internet connection"
                    )

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

                self.temperature_label.setText(
                    f"{temp_c:.0f}°C | {temp_f:.0f}°F")
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
        app = QApplication(sys.argv)
        weather_app = WeatherApp()
        weather_app.show()
        sys.exit(app.exec_())
