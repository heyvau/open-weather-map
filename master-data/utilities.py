import requests
from logger import log
import json

@log
def get_response(url: str, **payload) -> dict:
    """
    Function gets url with additional parameters and
    returns response to request as a dict. 
    """
    response = requests.get(url, params=payload)
    return response.json()


@log
def get_config(filename: str) -> dict:
    """
    Method reads config data from JSON file and returns it as a dict.
    """
    with open (filename, "r", encoding="UTF-8") as f:
        config_data = json.load(f)
    return config_data