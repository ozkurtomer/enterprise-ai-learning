import math
import requests

url = "http://localhost:11434/api/embed"
model = "bge-m3"

def get_embedding(text):
    payload = {
        "model": model,
        "input": text
    }

    response = requests.post(
        url,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"][0]

def cosine_similarity(vector1, vector2):
    dot_product = sum(
        a * b
        for a, b in zip(vector1, vector2)
    )

    magnitude1 = math.sqrt(
        sum(a * a for a in vector1)
    )

    magnitude2 = math.sqrt(
        sum(b * b for b in vector2)
    )

    return dot_product / (magnitude1 * magnitude2)

documents = [
    "Dependency Injection, bir sınıfın ihtiyaç duyduğu bağımlılıkların dışarıdan verilmesidir.",
    "Repository Pattern, veri erişim katmanını soyutlamak için kullanılan bir tasarım desenidir.",
    "Microservice mimarisi, uygulamanın küçük ve bağımsız servislerden oluşmasını sağlar.",
    "Bugün hava güneşli ve sıcak.",
    "SQL indexleri sorgu performansını artırmak için kullanılır."
]

document_embeddings = []

for document in documents:
    embedding = get_embedding(document)

    document_embeddings.append({
        "text": document,
        "embedding": embedding
    })

query = input("Aramak istediğiniz şeyi yazın: ")

query_embedding = get_embedding(query)


results = []

for document in document_embeddings:
    similarity = cosine_similarity(
        query_embedding,
        document["embedding"]
    )

    results.append({
        "text": document["text"],
        "score": similarity
    })


results.sort(
    key=lambda item: item["score"],
    reverse=True
)


print("\nSonuçlar:\n")

for result in results:
    print(
        f'Score: {result["score"]:.4f} | '
        f'{result["text"]}'
    )