import json
import requests

url = "http://localhost:11434/api/chat"

code = """
public async Task<User> GetUser(int id)
{
    return _context.Users.FirstOrDefault(x => x.Id == id);
}
"""

output_schema = {
    "type": "object",
    "properties": {
        "score": {
            "type": "integer"
        },
        "hasIssues": {
            "type": "boolean"
        },
        "summary": {
            "type": "string"
        },
        "issues": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "score",
        "hasIssues",
        "summary",
        "issues"
    ]
}

payload = {
    "model": "qwen3-coder:latest",
    "messages": [
        {
            "role": "system",
            "content": "Sen deneyimli bir C# code reviewerısın."
        },
        {
            "role": "user",
            "content": f"Aşağıdaki C# kodunu analiz et:\n\n{code}"
        }
    ],
    "stream": False,
    "format": output_schema,
    "options": {
        "temperature": 0
    }
}

response = requests.post(
    url,
    json=payload,
    timeout=120
)

response.raise_for_status()

data = response.json()

content = data["message"]["content"]

result = json.loads(content)

print("Score:", result["score"])
print("Problem Var mı?:", result["hasIssues"])
print("Özet:", result["summary"])
print("Problemler:", result["issues"])