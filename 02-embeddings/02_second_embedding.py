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


text1 = "Dependency Injection nedir?"
text2 = """
Dependency Injection, bir sınıfın ihtiyaç duyduğu
bağımlılıkların sınıf tarafından oluşturulması yerine
dışarıdan verilmesini sağlayan bir tasarım yaklaşımıdır.
"""
text3 = """
Bugün hava güneşli ve sıcak.
Akşam saatlerinde yağmur bekleniyor.
"""


embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)
embedding3 = get_embedding(text3)


similarity_1_2 = cosine_similarity(
    embedding1,
    embedding2
)

similarity_1_3 = cosine_similarity(
    embedding1,
    embedding3
)


print("Text 1:", text1)
print("Text 2:", text2)
print("Text 3:", text3)

print()

print("Text1 - Text2 benzerlik:", similarity_1_2)
print("Text1 - Text3 benzerlik:", similarity_1_3)