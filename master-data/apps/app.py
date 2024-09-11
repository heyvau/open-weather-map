from exporter import FileExporter
from db_manager import DBManager
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
        self.config = get_config(config_file)
        self.exporter = FileExporter()
        self.db_manager = DBManager(self.config["db"]["engine"])

    def export_to_file(self, data: list[dict]) -> None:
        """
        The method gets data and exports it to a file
        depending on the format specified in the configuration file.
        """
        for format_ in self.config["export_files"]:
            self.exporter.export(data=data, format=format_, filename=self.config["export_files"][format_])

    def export_to_db(self, data: list[dict]) -> None:
        self.db_manager.execute(self.config["db"]["stmt"]["drop_table"])
        self.db_manager.execute(self.config["db"]["stmt"]["create_table"])
        self.db_manager.execute(self.config["db"]["stmt"]["insert"], data=data)

    def run(self):
        """
        The method contains the main application logic.
        """
        data = self.get_data()
        self.export_to_file(data=data)
        self.export_to_db(data=data)
        # export to DB
        # create_owm_db()
        # self.exporter.export(data=self.cities, format="sql", table_name="CityWeather", db_name="owm.db"
