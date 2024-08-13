'''
Considere uma hierarquia de classes onde você tem uma classe base Animal e subclasses como Dog e Bird. Cada classe 
pode ou não ter um atributo específico, como fly ou bark. Crie uma função check_attribute_in_hierarchy que, dado um 
objeto, verifique se ele ou qualquer uma de suas classes pais possui um determinado atributo.Considere uma hierarquia 
de classes onde você tem uma classe base Animal e subclasses como Dog e Bird. Cada classe pode ou não ter um atributo 
específico, como fly ou bark. Crie uma função check_attribute_in_hierarchy que, dado um objeto, verifique se ele ou 
qualquer uma de suas classes pais possui um determinado atributo.
'''

class Animal:
    animais = []
    def __init__(self, nome):
        self.nome = nome
        self.animais.append(self)

class Passaro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        self.voar = True

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        self.andar = True

def chec_atributo(animal, atributo):
    print(f'{animal.nome} tem atributo {atributo} ' if hasattr(animal,atributo) else f'{animal.nome} não tem o atributo {atributo}')


pluto = Cachorro('Cachorro')
pit = Passaro('Passaro')

for animal in Animal.animais:
    chec_atributo(animal,'voar')