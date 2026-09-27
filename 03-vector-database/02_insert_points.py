import requests
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

ollama_url = "http://localhost:11434/api/embed"
embedding_model = "bge-m3"

qdrant_url = "http://localhost:6333"
collection_name = "software_documents"

def get_embedding(text):
    payload = {
        "model": embedding_model,
        "input": text
    }

    response = requests.post(
        ollama_url,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"][0]

client = QdrantClient(
    url=qdrant_url
)

documents = [
    {
        "id": 1,
        "text": "Dependency Injection, bir sınıfın ihtiyaç duyduğu bağımlılıkların dışarıdan verilmesidir.",
        "category": "architecture"
    },
    {
        "id": 2,
        "text": "SQL indexleri veritabanı sorgularının daha hızlı çalışmasını sağlamak için kullanılır.",
        "category": "database"
    },
    {
        "id": 3,
        "text": "Microservice mimarisinde uygulama birbirinden bağımsız küçük servislere ayrılır.",
        "category": "architecture"
    }
]

points = []

for document in documents:
    embedding = get_embedding(document["text"])

    point = PointStruct(
        id=document["id"],
        vector=embedding,
        payload={
            "text": document["text"],
            "category": document["category"]
        }
    )

    points.append(point)

client.upsert(
    collection_name=collection_name,
    points=points,
    wait=True
)

print(f"{len(points)} kayıt Qdrant'a eklendi.")