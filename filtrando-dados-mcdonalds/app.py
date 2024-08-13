'''
Exercício 2: Filtrando Dados de uma APIObjetivo: 
Filtrar dados de uma API e retornar apenas os itens de um restaurante 
específico.
'''

import requests #type: ignore
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print(f'Requisição não deu certo codigo {response.status_code}')
    exit()

restaurantes = {}

for item in data:
    nome_restaurante = item['Company']
    nome_comida = item['Item']
    if nome_restaurante not in restaurantes:
        restaurantes[nome_restaurante] = {}
    
    if nome_comida not in restaurantes[nome_restaurante]:
        restaurantes[nome_restaurante][nome_comida] = {
            'preco' : item['price'],
            'descricao' : item['description'] 
        }
for restaurante, itens in restaurantes.items():
    nome_arquivo = f'{restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(itens, arquivo_restaurante, indent=4)



    