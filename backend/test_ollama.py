from app.llm.ollama_client import OllamaClient

client = OllamaClient()

prompt = """
You are the AI reasoning engine of ECHO.

Analyze this memory.

Title:
Failed Interview

Description:
I studied for months but failed my coding interview today.

Return ONLY valid JSON.

{
  "sentiment": "",
  "emotion": "",
  "confidence": 0.0,
  "impact": {
    "Learning": 0,
    "Mood": 0,
    "Confidence": 0,
    "Career": 0,
    "Health": 0
  },
  "reason": ""
}

DO NOT WRITE ANYTHING EXCEPT JSON.
"""

response = client.generate(prompt)

print(response)