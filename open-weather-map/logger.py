import logging

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s (%(filename)s)\n%(name)s-%(levelname)s: %(message)s"
)

def log(func):
    """
    Decorator for error handling.
    """
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as error:
            logging.error(f"Error while executing <{func.__name__}>: {error}")
        else:
            logging.info(f"<{func.__name__}> finished successfully.")
            return res
    return wrapper