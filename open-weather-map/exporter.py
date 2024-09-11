from __future__ import annotations
import json
import yaml
import sqlite3
from logger import log


class FileExporter:
    def __init__(self):
        self._exporters = {
            "json": export_to_json,
            "yaml": export_to_yaml,
        }

    def export(self, data: list[dict], format: str, filename: str) -> function:
        """
        The method gets data and format for exporting and
        calls the executing function based on the passed format.
        """
        exporter = self._get_exporter(format)
        exporter(data, filename)

    @log
    def _get_exporter(self, format: str) -> function:
        """
        The method returns the executing function based on the passed format
        or raises error, when format is not supported.
        """
        exporter = self._exporters.get(format)
        if not exporter:
            raise ValueError(format)
        return exporter

@log
def export_to_json(data: list[dict], filename: str) -> None:
    """
    The function writes data to the json file.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4)

@log
def export_to_yaml(data: list[dict], filename: str) -> None:
    """
    The function writes data to the yaml file.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        yaml.dump(data, f, default_flow_style=False)
