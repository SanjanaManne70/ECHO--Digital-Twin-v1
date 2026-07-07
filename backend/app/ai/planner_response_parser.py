import json


class PlannerResponseParser:

    def parse(
        self,
        response,
    ):

        return json.loads(response)