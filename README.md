# Weather Now
## Project Introduction
Weather Now is a lightweight Python application that lets users quickly check real‑time weather conditions through both a graphical interface and a command‑line tool. The project demonstrates practical API integration, modular code structure, and a polished user experience.
The GUI, built with PyQt5, provides an intuitive interface for entering a city and instantly viewing temperature, conditions, and descriptive weather details. For users who prefer terminal workflows, the command-line (CLI) mode offers a simple dataset manager that can fetch, store, list, and delete weather entries.
Weather Now is built to be easy to run, easy to understand, and easy to extend. It’s a compact but complete example of:  
• 	API consumption using,   
• 	GUI development with PyQt5,  
• 	CLI design with argument parsing,  
• 	Simple project structure and maintainable code,  
• 	Real‑world features like configuration files and data persistence.

## Purpose of the app
## Target audience
## Features
## How it works
## External libraries used
## Attribution
## Screenshots
## Testing documentation  
Manual Testing Table — (PyQt5)/(GUI)
| Test ID | Scenario                            | Steps                                      | Expected Result | Actual Result | Status |
|---------|-------------------------------------|--------------------------------------------|-----------------|---------------|--------|
| T1      | Application launches                |Run   `weather_now.py`                      |                 |               |        |
| T2      | Empty city input                    |Leave input blank<br>→Click "Get Weather"   |                 |               |        |
| T3      | Missing creds.json                  |Remove/rename config.json<br>→ click button |                 |               |        |
| T4      | Invalid JSON in creds               |Break JSON syntax<br>→ run app              |                 |               |        |
| T5      | Missing API key field               |Remove key from config.json                 |                 |               |        |
| T6      | Invalid API key                     |Enter fake key<br>→ search city             |                 |               |        |
| T7      | Valid city                          |                                            |                 |               |        |
| T8      | Invalid city                        |                                            |                 |               |        |
| T9      | No internet                         |                                            |                 |               |        |
| T10     | API timeout                         |                                            |                 |               |        |
| T11     | API server error                    |                                            |                 |               |        |
| T12     | Loading state                       |                                            |                 |               |        |
| T13     | Button restores                     |                                            |                 |               |        |
| T14     | Emoji mapping                       |                                            |                 |               |        |
| T15     | Temperature conversion              |                                            |                 |               |        |
| T16     | Missing stylesheet                  |                                            |                 |               |        |
| T17     | Press `Enter` on keyboard to search |                                            |                 |               |        |
| T18     | Error clears on success             |                                            |                 |               |        |
| T19     | Weather clears on error             |                                            |                 |               |        |
| T20     | Application exit                    |                                            |                 |               |        |


## Development rationale
## Deployment instructions

## Project folder structure
weather_now/
```
├── weather_now.py         # Main GUI + CLI entry point
├── weather_api.py         # API communication module
├── cli.py                 # CLI logic
├── run.py                 # Simple launcher used for testing the virtual environment
├── styles.qss             # GUI stylesheet
├── creds.json             # User-provided API key (not included in repo)
├── weather_history.json   # CLI dataset (ignored)
├── .flake8                # Linting configuration for enforcing consistent code style

├── requirements.txt       # Python dependencies
├── .gitignore             # Files and folders excluded from Git tracking
└── README.md              # Project documentation
```

 ## WInstallation & Usage Guide
 ### Installation
 **Clone the repository:**  
 `git clone https://github.com/<your-username>/weather_now.git`
`cd weather_now`  
Install the required dependencies:
`pip install -r requirements.txt`
This installs:  
• 	PyQt5 — for the GUI.  
• 	requests — for API communication.  

**API Key Setup (Required):**  
Weather Now uses the OpenWeather API.
Before running the app, create a file named:
`creds.json`.
Place it in the project root with the following structure:
`{
    "api": {
        "key": "YOUR_API_KEY_HERE"
    }
}`
You can obtain a free API key from:
https://openweathermap.org/api.  
If the key is missing or invalid, the app will run but will display an error when fetching weather data.
### Running the Graphical User Interface
To launch the graphical user interface, enter:  
`python weather_now.py`  

The GUI allows you to:  
• 	Enter a city name.  
• 	Fetch current weather.  
• 	View temperature in °C and °F.  
• 	See weather conditions with emojis.  
• 	Read a short description.   

Weather Now also includes a command‑line interface for managing a simple weather dataset.
### Run in command-line mode:
`python weather_now.py --cli`  

Commands
| Command          | Description                               |
|------------------|-------------------------------------------|
| `add <city>`     | Fetches weather for a city and saves it   |
| `list`           | Displays all saved weather entries        |
| `delete <index>` | Removes an entry by its list number       |
| `exit`           | Exits the CLI mode                        |

The dataset is stored in:  
`weather_history.json`  
This file is ignored by Git to avoid committing user‑specific data.

 


