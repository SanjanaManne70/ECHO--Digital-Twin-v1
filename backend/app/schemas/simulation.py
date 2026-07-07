from pydantic import BaseModel


class SimulationRequest(BaseModel):

    scenario: str