import requests

url = "http://localhost:11434/api/chat"

question = input("Sorunuz: ")

payload = {
    "model": "qwen3-coder:latest",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ],
    "stream": False
}

response = requests.post(
    url,
    json=payload,
    timeout=120
)

response.raise_for_status()

data = response.json()

answer = data["message"]["content"]

print("AI:", answer)