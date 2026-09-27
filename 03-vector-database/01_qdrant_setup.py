from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


client = QdrantClient(
    url="http://localhost:6333"
)

collection_name = "software_documents"


if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=1024,
            distance=Distance.COSINE
        )
    )

    print("Collection oluşturuldu.")

else:
    print("Collection zaten mevcut.")