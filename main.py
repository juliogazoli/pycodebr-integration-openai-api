from decouple import config
from openai import OpenAI

client = OpenAI(
    api_key=config('API_KEY'),
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Você será um tradutor de textos de português para inglês. Apenas traduza e responda a tradução do texto que você receber.'
        },
        {
            'role': 'user',
            'content': 'O livro está na mesa.'
        },
    ],
    # max_tokens=150,
    # temperature=0.2,
)

print(response.choices[0].message.content)
