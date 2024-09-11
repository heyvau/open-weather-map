from apps.owm_app import OwmApp
from apps.currency_app import CurrencyApp
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

OWM_CONFIG_FILE = "./configs/owm_config.json"
CURRENCY_CONFIG_FILE = "./configs/currency_config.json"

if __name__ == "__main__":
    for app in [OwmApp(OWM_CONFIG_FILE), CurrencyApp(CURRENCY_CONFIG_FILE)]:
        app.run()
