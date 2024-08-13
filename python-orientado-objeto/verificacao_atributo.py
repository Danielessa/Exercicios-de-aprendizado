'''
1. Verificação de Tipo de Objeto
Escreva uma função verificar_inteiro(obj) que recebe um objeto obj como argumento. A função deve retornar True se 
o objeto for um inteiro, e False caso contrário. Use isinstance para fazer essa verificação.'''
class Verificador:
    def verificar_inteiro(self, valor):
        return isinstance(valor, int)
        


v = int(input('Digite um valor: '))

verify = Verificador()
print(verify.verificar_inteiro(v))
resposta = f'{v} é uma instancia de int()' if verify.verificar_inteiro(v)  else f'{v} não é uma instancia de int()'
print(resposta)
