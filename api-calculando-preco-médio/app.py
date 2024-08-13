import requests #type: ignore

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

else:
    print(f'Falha ao importar dados. Código {response.status_code}')
    exit()

restaurantes = {}
for elemento in data:
    nome_restaurante = elemento['Company']
    preco = elemento['price']
    if nome_restaurante not in restaurantes:
        restaurantes[nome_restaurante] = [0,0]
        

    restaurantes[nome_restaurante][0] += preco
    restaurantes[nome_restaurante][1] += 1


for restaurante, preco_total in restaurantes.items():
    print(f'{restaurante}: {preco_total[0]:.2f}')
    print(f'Numero de itens: {preco_total[1]:.2f}')
    preco_medio = preco_total[0]/preco_total[1]
    print(f'Preço médio: {preco_medio:.2f}\n')


