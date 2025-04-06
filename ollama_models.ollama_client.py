# ollama_models/ollama_client.py
import ollama

def query_ollama(prompt, model="phi"):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

