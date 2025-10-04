import requests
import json

prompt = "Explain how neural networks learn, in simple terms."

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": prompt
    },
    stream=True  # stream=True lets you get tokens as they generate
)

for line in response.iter_lines():
    if line:
        data = json.loads(line)
        print(data.get("response", ""), end="", flush=True)