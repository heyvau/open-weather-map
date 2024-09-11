from logger import log
from utilities import get_response
from apps.app import AppABC, App


class CurrencyApp(App, AppABC):
    """
    Application for currency API.
    """
    @log
    def _fetch_currency_data(self, cur_code: str) -> dict:
        """
        The method gets currency code and returns 
        exchange rate data as a dict.
        """
        current_data = get_response(
            url=self.config["url"],
            access_key=self.config["api_key"]
        )
        currency = current_data["rates"][cur_code]
        return {
                f"EUR_{cur_code}": round(currency, 2),
                f"{cur_code}_EUR": round(1 / currency, 2)
            }

    @log
    def get_data(self):
        """
        The method returns exchange rate data
        for all specified currency codes. 
        """
        currencies = []
        for cur_code in self.config["currency"]["EUR"]:
            currencies.append(self._fetch_currency_data(cur_code))
        return currencies