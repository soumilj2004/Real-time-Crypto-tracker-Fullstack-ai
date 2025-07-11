import requests
import os
from dotenv import load_dotenv

load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://localhost:11434")

def query_ollama(prompt: str, model: str = "mistral"):
    response = requests.post(f"{OLLAMA_URL}/api/chat", json={
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    })
    return response.json()["message"]["content"]
