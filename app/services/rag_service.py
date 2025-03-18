import os

from openai import OpenAI

from app.services.cache_service import cache_response

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@cache_response(ttl=3600)  # Cache de 1 hora
def generate_answer(question: str, context: str):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}\nAnswer:"},
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
