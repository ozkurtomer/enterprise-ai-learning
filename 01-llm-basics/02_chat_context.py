import requests

url = "http://localhost:11434/api/chat"

messages = [
    {
        "role": "system",
        "content": "Sen yardımcı, kısa ve anlaşılır cevaplar veren bir asistansın."
    }
]

while True:
    question = input("Sen: ")

    if question.lower() == "exit":
        break

    messages.append({
        "role": "user",
        "content": question
    })

    payload = {
        "model": "qwen3-coder:latest",
        "messages": messages,
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

    messages.append({
        "role": "assistant",
        "content": answer
    })