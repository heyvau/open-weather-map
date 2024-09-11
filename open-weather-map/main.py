from owm_app import OwmApp
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

OWM_CONFIG_FILE = "./owm_config.json"

if __name__ == "__main__":
    owm = OwmApp(OWM_CONFIG_FILE)
    owm.run()
