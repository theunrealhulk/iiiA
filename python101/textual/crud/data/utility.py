import json
from pathlib import Path
class Utility():
    @staticmethod
    def loadData(path:str="data.json"):
        path = Path(__file__).parent.parent / 'data' / 'data.json'
        """Load a JSON file and return it as a list."""
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)