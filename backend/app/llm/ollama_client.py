from ollama import chat


class OllamaClient:

    def __init__(self):
        self.model = "mistral:latest"

    def generate(self, prompt: str):

        print("\n========== CALLING OLLAMA ==========\n")

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        print("\n========== OLLAMA FINISHED ==========\n")

        return response["message"]["content"]