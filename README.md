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
Weather Now was built to explore how real‑time data, clean UI design, and modular Python architecture can come together in a practical, everyday tool. The project demonstrates how to integrate external APIs, manage configuration securely, and deliver the same functionality through both a graphical interface and a command‑line workflow.
At its core, the app exists to answer a simple question—“What’s the weather like right now?”—but it does so in a way that highlights good engineering practices: isolated virtual environments, reproducible dependencies, structured modules, and a clear separation between logic and presentation.
The project also serves as a learning platform, showcasing how Python applications can be packaged, documented, and deployed in a way that mirrors real‑world development standards.
## Target audience
Weather Now is designed for a broad range of users, each benefiting from a different aspect of the application:
• 	Everyday users who want a quick, clean way to check current weather conditions without navigating ads or cluttered websites.
• 	Developers and students looking for a reference project that demonstrates API integration, PyQt5 GUI design, CLI tooling, and modular Python structure.
• 	Educators and reviewers assessing code quality, documentation, reproducibility, and adherence to best practices in a small but complete software project.
• 	Command‑line enthusiasts who prefer fast, scriptable weather lookups directly from the terminal.
• 	Learners exploring Python environments who want to understand how virtual environments, configuration files, and dependency management work in practice.
Weather Now is intentionally simple on the surface but structured in a way that encourages exploration, extension, and adaptation.
## Features
Dual Interface
• 	GUI Mode powered by PyQt5 for an interactive, user‑friendly experience.
• 	CLI Mode for quick weather lookups directly from the terminal.
• 	Real‑Time Weather Data
• 	Fetches current conditions (temperature, humidity, wind, etc.) from the OpenWeather API.
• 	Config‑Driven Setup
• 	API key and default settings stored in a  file.
• 	Keeps sensitive data out of source control.
• 	Isolated Virtual Environment
• 	Uses a project‑local  to ensure clean, reproducible dependencies.
• 	 is intentionally excluded from version control.
• 	Modular Codebase
• 	Clear separation between API logic, UI components, and CLI handlers.
• 	Easy to extend or integrate into other projects.
## Future Enhancements
Weather Now is intentionally lightweight, but there are several meaningful improvements planned to expand its capabilities and refine the user experience. These enhancements aim to make the application more informative, more customizable, and more adaptable to different usage styles.
🔧 Planned Features
• 	5‑Day Forecast Support
Extend the current real‑time weather lookup with multi‑day forecasts, including temperature trends, precipitation probability, and wind patterns.
• 	Search History & Favorites
Allow users to save frequently checked locations and quickly revisit previous searches in both GUI and CLI modes.
• 	Improved Error Handling & Offline Mode
Provide clearer feedback when API requests fail and offer a fallback mode that displays the last known weather data.
• 	Unit & Language Customization
Add support for switching between Celsius/Fahrenheit, metric/imperial units, and multiple UI languages.
• 	Enhanced GUI Features
Introduce icons, themes, and layout improvements to make the interface more visually engaging and accessible.
• 	Packaging & Distribution
Package the app as a standalone executable for Windows, making installation easier for non‑technical users.
• 	Plugin‑Friendly Architecture
Explore a modular system where additional data sources (e.g., air quality, UV index, sunrise/sunset times) can be added as optional extensions.
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
The following flowchart illustrates the core logic behind Weather Now, showing how the application processes user input, retrieves data from the OpenWeather API, and displays results in both GUI and CLI modes. This visual overview helps clarify the internal structure of the project and highlights how each component interacts within the overall system.
![Application flowchart](weather_now/images/app_flowchart.png)

## Data Flow Diagram
The Data Flow Diagram (DFD) provides a high‑level view of how information moves through Weather Now, from user input to API communication and final output. It highlights the major data sources, processing steps, and outputs that make up the core functionality of the application.
This diagram helps clarify how the system handles requests, transforms raw API data, and delivers weather information through both the GUI and CLI interfaces.







