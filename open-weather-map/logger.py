import logging
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(name)s-%(levelname)s\n%(message)s"
)

def log(func):
    """
    Decorator for error handling.
    """
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as error:
            logging.error(
                f"Error while executing {func.__name__}() *{func.__module__}*: {error}")
        else:
            logging.info(
                f"{func.__name__}() *{func.__module__}* finished successfully.")
            return res
    return wrapper
