import json
import requests

url = "http://localhost:11434/api/chat"
model = "qwen3-coder:latest"

question = input("Sorunuz: ")

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ],
    "stream": True
}

try:
    response = requests.post(
        url,
        json=payload,
        timeout=120,
        stream=True
    )

    response.raise_for_status()

    print("AI: ", end="", flush=True)

    for line in response.iter_lines():

        if not line:
            continue

        data = json.loads(line.decode("utf-8"))

        content = data["message"]["content"]

        print(content, end="", flush=True)

        if data["done"]:
            break

    print()

except requests.exceptions.ConnectionError:
    print("Ollama servisine bağlanılamadı.")

except requests.exceptions.Timeout:
    print("Model belirtilen sürede cevap vermedi.")

except requests.exceptions.RequestException as error:
    print("İstek sırasında hata oluştu:", error)