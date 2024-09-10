from __future__ import annotations
import json
import yaml
import sqlite3


class DataExporter:
    def __init__(self):
        self._exporters = {
            "json": export_to_json,
            "yaml": export_to_yaml,
            "sql": export_to_sql
        }

    def export(self, data: list[dict], format: str, **kwargs) -> function:
        """
        Method gets data and format for exporting and
        calls the executing function based on the passed format.

        Other required keyword arguments:
        - export to file: 
            filename(str)
        - export to db:
            table_name(str)
            db_name(str)
        """
        exporter = self._get_exporter(format)
        exporter(data, **kwargs)

    def _get_exporter(self, format: str) -> function:
        """
        Method returns the executing function based on the passed format
        or raises error, when format is not supported.
        """
        exporter = self._exporters.get(format)
        if not exporter:
            raise ValueError(format)
        return exporter


def export_to_json(data: list[dict], filename: str) -> None:
    """
    Function writes data to the json file.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4)


def export_to_yaml(data: list[dict], filename: str) -> None:
    """
    Function writes data to the yaml file.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        yaml.dump(data, f, default_flow_style=False)


def export_to_sql(data: list[dict], table_name: str, db_name: str) -> None:
    """
    Function inserts data rows into the db table.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    fields = tuple(data[0].keys())
    values = [tuple(i.values()) for i in data]
    
    sql_statement = f'INSERT INTO {table_name} \
        {fields} \
        VALUES({", ".join(["?"] * len(fields))});'

    with conn:
        cursor.executemany(sql_statement, values)
