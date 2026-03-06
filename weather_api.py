import json
import requests
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_api_key():
    try:
        config_path = resource_path("config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
            return config["api"]["key"]
    except:
        return None
