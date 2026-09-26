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
    "stream": False,
    "options": {
        "temperature": 0.2,#daha yaratıcı cevaplar için 0.7-1.0 arası değerler kullanılabilir. Düşük değerler daha deterministik ve güvenilir cevaplar üretir.
        "top_p": 0.9,
        "num_predict": 150#max token sayısı. Daha uzun cevaplar için artırılabilir. Modelin max token limitini aşmamak gerekir.
    }
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