from app.llm.ollama_client import OllamaClient


class PlannerAgent:

    def __init__(self):

        self.client = OllamaClient()

    def generate(
        self,
        analysis,
        context,
    ):

        prompt = f"""
You are ECHO.

You are an AI Daily Planner.

Current Digital Twin

{context["twin"]}

Recent Memories

{context["memories"]}

Latest Analysis

Emotion:
{analysis.emotion}

Sentiment:
{analysis.sentiment}

Severity:
{analysis.severity}

Reason:
{analysis.reason}

Generate ONE action the user should do next.

Return ONLY valid JSON.

Example:

{{
    "title":"Sleep before 11 PM",
    "description":"Avoid screens after 10:30 PM.",
    "priority":"High"
}}

Do not return markdown.
Do not explain anything.
"""

        return self.client.generate(
            prompt,
        )