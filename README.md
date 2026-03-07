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
| Test ID | Scenario                            | Steps                                        | Expected Result                          | Actual Result |
|---------|-------------------------------------|----------------------------------------------|------------------------------------------|---------------|
| T1      | Application launches                |Run   `weather_now.py`                        |GUI window opens with all widgets visible |As expected    |
| T2      | Empty city input                    |Leave input blank<br>→Click "Get Weather"     |Error: “Please enter a city name.”        |As expected    |
| T3      | Missing creds.json                  |Remove/rename config.json<br>→ click button   |Error: “API key missing…”                 |As expected    |
| T4      | Invalid JSON in creds               |Break JSON syntax<br>→ run app                |Error: “API key missing…”                 |As expected    |
| T5      | Missing API key field               |Remove `key` from creds.json                  |Error: “API key missing…”                 |As expected    |
| T6      | Invalid API key                     |Enter fake key<br>→ search city               |Error: “Unauthorized: Invalid API key”    |As expected    |
| T7      | Valid city                          |Enter, for example “London”<br>→ click button |Weather data displayed                    |As expected    |
| T8      | Invalid city                        |Enter for example “asdfgh”<br>→ click button  |Error: “City not found”                   |As expected    |
| T9      | No internet                         |Disable internet connection<br> → click button|Error: “Connection Error…”                |As expected    |
| T10     | API timeout                         |Simulate slow network                         |Error: “Timeout Error…”                   |As expected    |
| T11     | API server error                    |Force 500 response                            |Error: “Server error…”                    |As expected    |
| T12     | Loading state                       |Click button                                  |Button shows “Loading…” and disables      |As expected    |
| T13     | Button restores                     |After request completes                       |Button returns to normal                  |As expected    |
| T14     | Emoji mapping                       |Test weather types                            |Correct emoji displayed                   |As expected    |
| T15     | Temperature conversion              |Compare °C/°F                                 |Correct conversion shown                  |As expected    |
| T16     | Missing stylesheet                  |Remove style.qss                              |Console warning, but app still works      |As expected    |
| T17     | Press `Enter` on keyboard to search |Type city<br>→ press Enter                    |Same as clicking button                   |As expected    |
| T18     | Error clears on success             |Trigger error<br>→ then valid city            |Error label clears                        |As expected    |
| T19     | Weather clears on error             |Show weather<br>→ then trigger error          |Weather labels clear                      |As expected    |
| T20     | Application exit                    |Close window                                  |App exits cleanly                         |As expected    |


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
 ### Requirements
• 	Python v3.10 or later  
• 	Internet connection (for API requests)  
• 	OpenWeatherMap API key  
• 	Required Python packages: `PyQt5` `requests`

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
### Usage Notes 
•  If the API key is missing or invalid, the app will show a clear error message.  
• 	If the city name is empty or incorrect, the app will notify the user.  
• 	If the internet connection is unavailable, the app will display a connection error.  
• 	The button disables during loading to prevent duplicate requests.  
• 	The app uses an external stylesheet () for visual styling.
### Troubleshooting
|Issue              |Cause                        |Solution                  |
|-------------------|-----------------------------|--------------------------|
|"API key missing"  |creds.json missing or invalid|Recreate creds.jsson      |
|"City not found"   |Invalid city name            | Check spelling           |
|"Connection Error" |No internet                  |Reconnect and retry       |
|No styling applied |Missing `style.qss`          |Add or recreate stylesheet|

## Application Flowchart (PyQt5 GUI)
![Application flowchart](weather_now/app_flowchart.png)




