import json
import requests
from exporter import DataExporter
from abc import ABC, abstractmethod


def get_response(url: str, **payload) -> dict:
    """
    Function gets url with additional parameters and
    returns response to request as a dict. 
    """
    response = requests.get(url, params=payload)
    return response.json()


class App(ABC):
    def __init__(self, config_file: str) -> None:
        self.exporter = DataExporter()
        self.config = self.get_config(config_file)

    def get_config(self, filename: str) -> dict:
        """
        Method reads config data from JSON file and returns it as a dict.
        """
        with open (filename, "r", encoding="UTF-8") as f:
            config_data = json.load(f)
        return config_data

    @abstractmethod
    def run():
        """
        Method contains the main application logic.
        """
        pass


class OwmApp(App):
    """
    Application for Open Weather Map.
    """
    def __init__(self, config_file: str) -> None:
        super().__init__(config_file)
        self.cities = []

    def get_city_data(self, city: str) -> dict:
        """
        Method gets name of the city and returns 
        its current weather data as a dict. 
        """
        current_data = get_response(
            url=self.config["url"],
            q=city, appid=self.config["api_key"],
            units=self.config["units"], lang=self.config['languages'][0]
        )
        city_data = {
            "city": current_data["name"],
            "temperature_C": current_data["main"]["temp"],
            "humidity": current_data["main"]["humidity"],
            f"description_{self.config['languages'][0]}": current_data["weather"][0]["description"]
        }
        for lang in self.config.get("languages")[1:]:
            current_data = get_response(
                url=self.config["url"],
                q=city, appid=self.config["api_key"],
                units=self.config["units"], lang=lang
            )
            city_data.update({
                f"description_{lang}": current_data["weather"][0]["description"]
            })
        return city_data

    def run(self):
        for city in self.config["cities"]:
            self.cities.append(self.get_city_data(city))

        # export to files
        for format_ in self.config["export_files"]:
            self.exporter.export(data=self.cities, format=format_, filename=self.config["export_files"][format_])
        # export to DB
        self.exporter.export(data=self.cities, format="sql", table_name="CityWeather", db_name="owm.db")
