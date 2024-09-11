from logger import log
from utilities import get_response
from apps.app import AppABC, App


class OwmApp(App, AppABC):
    """
    Application for Open Weather Map.
    """
    @log
    def _fetch_city_data(self, city: str) -> dict:
        """
        The method gets name of the city and returns 
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
        for lang in self.config["languages"][1:]:
            current_data = get_response(
                url=self.config["url"],
                q=city, appid=self.config["api_key"],
                units=self.config["units"], lang=lang
            )
            city_data.update({
                f"description_{lang}": current_data["weather"][0]["description"]
            })
        return city_data

    @log
    def get_data(self) -> list[dict]:
        """
        The method returns weather data
        for all specified cities. 
        """
        cities = []
        for city in self.config["cities"]:
            cities.append(self._fetch_city_data(city))
        return cities
