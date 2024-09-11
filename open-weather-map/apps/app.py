from exporter import FileExporter
from abc import ABC, abstractmethod
from utilities import get_config


class AppABC(ABC):
    """
    Abstract class for application.
    """
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def export_to_file(self):
        pass

    @abstractmethod
    def run(self):
        pass


class App:
    """
    Base application class.
    """
    def __init__(self, config_file: str) -> None:
        self.exporter = FileExporter()
        self.config = get_config(config_file)

    def export_to_file(self, data: str) -> None:
        """
        The method gets data and exports it to a file
        depending on the format specified in the configuration file.
        """
        for format_ in self.config["export_files"]:
            self.exporter.export(data=data, format=format_, filename=self.config["export_files"][format_])

    def run(self):
        """
        The method contains the main application logic.
        """
        data = self.get_data()
        self.export_to_file(data)
        # export to DB
        # create_owm_db()
        # self.exporter.export(data=self.cities, format="sql", table_name="CityWeather", db_name="owm.db")

