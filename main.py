from decouple import config
from openai import OpenAI

client = OpenAI(
    api_key=config('API_KEY'),
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': 'Fale sobre o Fiat Elba 1988'},
    ],
)

print(response.choices[0].message.content)
