class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        

class Sedan(Veiculo):
    def __init__(self, marca, ano, velocidade_max):
        super().__init__(marca, ano)
        self.velocidade_max = velocidade_max

    def ligar_carro(self):
        self.ligado = True

class Corrida:
    def __init__(self,nome, premiacao, tamanho_pista):
        self.nome = nome
        self.premiacao = premiacao
        self.__tamanho_pista = tamanho_pista

    def inscricao(self, inscritos):
        self.corredores = inscritos
    
    @property
    def correr(self):
        
        for corredor in self.corredores:
            try:
                if corredor.velocidade_max > maior_corredor.velocidade_max:
                    maior_corredor = corredor

            except:
                maior_corredor = corredor

        self.vencedor = maior_corredor
    
    @property
    def tempo_vencedor(self):
        self.tempo = self.__tamanho_pista/(self.vencedor.velocidade_max/3.6)
        return self.tempo
        

civic = Sedan('Honda', 2017, 180)
classic = Sedan('Classic', 2022, 110)
hb20s = Sedan("HB20's", 2016, 130)

f1_amador = Corrida('F1 amador', 500000, 3250)

inscritos = [civic, classic, hb20s]

f1_amador.inscricao(inscritos)
f1_amador.correr


print(f'O vencedor é {f1_amador.vencedor.marca} com uma velocidade máxima de {f1_amador.vencedor.velocidade_max}Km/H com um tempo de {f1_amador.tempo_vencedor} segundos')