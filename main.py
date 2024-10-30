from decouple import config
from openai import OpenAI

client = OpenAI(
    api_key=config('API_KEY'),
)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        # {'role': 'system', 'content': 'Você é um assistente virtual especializado em carro e mecânica automotiva. Dê respostas técnicas sobre mecânica.'},
        # {'role': 'user', 'content': 'Fale sobre o Chevrolet Cobalt'},

        {'role': 'system', 'content': 'Dê respostas técnicas sobre programação. Se comporte como um programador Python experiente, especialista de projetos e arquitetura limpa.'},
        {'role': 'user', 'content': 'Me mostre como posso fazer um projeto Django com as melhores boas práticas.'},
    ],
)

print(response.choices[0].message.content)
