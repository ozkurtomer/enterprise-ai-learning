import requests
from qdrant_client import QdrantClient

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

query = input("Aramak istediğiniz şeyi yazın: ")

query_embedding = get_embedding(query)

search_result = client.query_points(
    collection_name=collection_name,
    query=query_embedding,
    limit=3,
    with_payload=True
)

print("\nEn alakalı sonuçlar:\n")

for index, point in enumerate(
    search_result.points,
    start=1
):
    print(f"{index}. Score: {point.score:.4f}")
    print(f"Text: {point.payload['text']}")
    print(f"Category: {point.payload['category']}")
    print()