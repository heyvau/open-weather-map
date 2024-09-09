import json
from pathlib import Path
import requests
from exporter import DataExporter


CONFIG_FILE = "./config.json"


def get_config(filename: str) -> dict:
    """
    Function reads config data from JSON file and returns it as a dict.
    """
    with open (Path(__file__).parent / filename, "r", encoding="UTF-8") as f:
        config_data = json.load(f)
    return config_data


def get_current_city_weather(city:str, api_key: str,  unit: str, lang: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}&lang={lang}"
    response = requests.get(url)
    return response.json()


def app(config_file: str):
    """
    Main function.
    """
    config = get_config(config_file)

    exporter = DataExporter()
    cities = []

    for city in config.get("cities"):

        city_data = {}

        current_data = get_current_city_weather(
            city=city, api_key=config["api_key"],
            unit=config["unit"], lang=config['languages'][0]
        )

        city_data.update({
            "city": current_data["name"],
            "temperature_C": current_data["main"]["temp"],
            "humidity": current_data["main"]["humidity"],
            f"description_{config['languages'][0]}": current_data["weather"][0]["description"]
        })
        

        for lang in config.get("languages")[1:]:
            current_data = get_current_city_weather(
                city=city, api_key=config["api_key"],
                unit=config["unit"], lang=lang
            )

            city_data.update({
                f"description_{lang}": current_data["weather"][0]["description"]
            })
        
        cities.append(city_data)
    exporter.export(data=cities, filename=config.get("export_file"), format="json")


if __name__ == "__main__":
    app(CONFIG_FILE)