from __future__ import annotations
import json
from pathlib import Path

class DataExporter:
    def __init__(self):
        self._exporters = {
            "json": export_to_json
        }

    def export(self, data: list[dict], filename: str, format: str) -> function:
        export = self._get_exporter(format)
        export(data, filename)

    def _get_exporter(self, format: str) -> function:
        exporter = self._exporters.get(format)
        if not exporter:
            raise ValueError(format)
        return exporter


def export_to_json(data: list[dict], filename: str):
    with open(Path(__file__).parent / filename, mode="w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4)
