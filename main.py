from decouple import config
from openai import OpenAI

client = OpenAI(
    api_key=config('API_KEY'),
)

stream = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'user', 'content': 'Fale sobre o Fiat Elba 1988'},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')
