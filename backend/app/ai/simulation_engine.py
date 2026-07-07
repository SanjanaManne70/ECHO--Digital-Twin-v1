from app.ai.simulation_prompt import SimulationPrompt
from app.ai.response_parser import ResponseParser
from app.llm.ollama_client import OllamaClient


class SimulationEngine:

    def __init__(self):

        self.prompt = SimulationPrompt()

        self.client = OllamaClient()

        self.parser = ResponseParser()

    def simulate(

        self,

        scenario,

        current_state,

        goals,

    ):

        prompt = self.prompt.build(

            scenario,

            current_state,

            goals,

        )

        raw = self.client.generate(prompt)

        print("\n========== SIMULATION ==========\n")
        print(raw)
        print("\n================================\n")

        return self.parser.parse_simulation(raw)