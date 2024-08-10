class Frase:
    def __init__(self, texto):
        self._texto = texto

    @property
    def texto(self):
        return self._texto
    
    @property
    def contador_palavras(self):
        n = self._texto.count(' ')
        return n+1
    
t = input('Escreva uma frase: ')
text = Frase(t)
print(text.texto)
print(text.contador_palavras)
