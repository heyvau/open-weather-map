from exporter import FileExporter
from abc import ABC, abstractmethod
from utilities import get_config


class AppABC(ABC):
    @abstractmethod
    def get_data(self):
        raise NotImplementedError


class App:
    def __init__(self, config_file: str) -> None:
        self.exporter = FileExporter()
        self.config = get_config(config_file)

    def run(self):
        """
        Method contains the main application logic.
        """
        data = self.get_data()
        self.export_to_file(data)

    def export_to_file(self, data):
        for format_ in self.config["export_files"]:
            self.exporter.export(data=data, format=format_, filename=self.config["export_files"][format_])




        # export to DB
        # create_owm_db()
        # self.exporter.export(data=self.cities, format="sql", table_name="CityWeather", db_name="owm.db")

