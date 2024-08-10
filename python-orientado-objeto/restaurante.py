import os

class Restaurante:
    nome = ''
    categoria = ''
    status = False

def criando_restaurantes():
    praca = Restaurante()
    praca.nome = 'Restaurante Praça'
    praca.categori = 'Gourmet'

    pizzaria = Restaurante()
    pizzaria.nome = 'Pizzaria'
    pizzaria.categoria = 'Italiana'

    global lista_restaurantes 
    
    lista_restaurantes = [praca, pizzaria]


def mostrar_restaurante():
    for mostrar_restaurante in lista_restaurantes:
        print(f'Nome: {mostrar_restaurante.nome}')
        print(f'Categoria: {mostrar_restaurante.categoria}')
        print(f'Status: {mostrar_restaurante.status}')
        print('='*20,'\n')


os.system('cls')
criando_restaurantes()
mostrar_restaurante()


