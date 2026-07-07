import json
from pathlib import Path


class ImpactEngine:

    def __init__(self):

        file_path = (
            Path(__file__).parent.parent
            / "knowledge"
            / "impact_rules.json"
        )

        with open(file_path, "r") as file:
            self.rules = json.load(file)

    def calculate(self, domain):

        return self.rules.get(
            domain,
            {},
        )