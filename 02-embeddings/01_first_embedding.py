import requests

url = "http://localhost:11434/api/embed"

payload = {
    "model": "nomic-embed-text",
    "input": "Dependency Injection nedir?"
}

response = requests.post(
    url,
    json=payload,
    timeout=120
)

response.raise_for_status()

data = response.json()

embedding = data["embeddings"][0]

print("Vector uzunluğu:", len(embedding))
print("İlk 10 değer:", embedding[:10])