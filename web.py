from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Weather CLI is deployed and running on Heroku. Use 'heroku run' to execute CLI commands."