import requests

url = "http://localhost:11434/api/chat"
model = "qwen3-coder:latest"


def ask_llm(question):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "Ollama servisine bağlanılamadı."

    except requests.exceptions.Timeout:
        return "Model belirtilen sürede cevap vermedi."

    except requests.exceptions.HTTPError as error:
        return f"HTTP hatası oluştu: {error}"

    except requests.exceptions.RequestException as error:
        return f"İstek sırasında hata oluştu: {error}"


question = input("Sorunuz: ")

answer = ask_llm(question)

print("AI:", answer)