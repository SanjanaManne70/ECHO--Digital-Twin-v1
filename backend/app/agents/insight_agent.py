from app.llm.ollama_client import OllamaClient


class InsightAgent:

    def __init__(self):

        self.client = OllamaClient()

    def generate(
        self,
        analysis,
        context,
    ):

        twin = context["twin"]

        memories = context["memories"]

        prompt = f"""
You are ECHO.

You are the user's AI Digital Twin.

Your job is to generate ONE useful insight based ONLY on the user's current state.

Current Digital Twin

{twin}

Recent Memories

{memories}

Latest Analysis

Emotion:
{analysis.emotion}

Sentiment:
{analysis.sentiment}

Severity:
{analysis.severity}

Reason:
{analysis.reason}

Instructions:

- Use ONLY the provided information.
- Do NOT invent facts.
- Explain the most important pattern you notice.
- Mention how the latest event affects the user's overall state.
- Give ONE short actionable recommendation.
- Keep the response under 100 words.
- Return plain text only.

"""

        response = self.client.generate(
            prompt,
        )

        return response