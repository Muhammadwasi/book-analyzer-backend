# groq_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv

class GroqClient:
    def __init__(self, model: str = "meta-llama/llama-4-scout-17b-16e-instruct", temperature: float = 0.2):
        load_dotenv()
        self.model = model
        self.temperature = temperature
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def ask_as_user(self, messages: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": messages}],
            temperature=self.temperature,
        )
        return response.choices[0].message.content
