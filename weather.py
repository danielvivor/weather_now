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

# Start the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
