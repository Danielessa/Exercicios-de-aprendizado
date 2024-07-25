import os

class ContaBancaria:
    contas = []
    
    def __init__(self, N_conta, titular, saldo):
        self.N_conta = N_conta
        self.titular = titular
        self.saldo = saldo
        ContaBancaria.contas.append(self)
        self.proxima_acao()

    @classmethod
    def encontrar_conta(cls):
        titular = input('Quem é o titular da conta?\n')
        for usuario in cls.contas:
            if usuario.titular == titular:
                return usuario

    def verificar_conta(self):
        usuario = self.encontrar_conta()
        if usuario:
            print(f'N_conta: {usuario.N_conta}')
            print(f'Titular: {usuario.titular}')
            print(f'Saldo: {usuario.saldo}')
        else:
            print('Conta não encontrada.')
        self.proxima_acao()
    
    def depositar(self, v_deposito):
        usuario = self.encontrar_conta()
        if usuario:
            print(f'Foi depositado R$ {v_deposito} na sua conta')
            usuario.saldo += v_deposito
        else:
            print('Conta não encontrada.')
        self.proxima_acao()

    def sacar(self, v_saque):
        usuario = self.encontrar_conta()
        if usuario:
            print(f'Foi sacado R$ {v_saque} da sua conta')
            usuario.saldo -= v_saque
        else:
            print('Conta não encontrada.')
        self.proxima_acao()

    def menu(self):
        print('MENU\n')
        print('1 - Verificar conta')
        print('2 - Cadastrar conta')
        print('3 - Deposito')
        print('4 - Saque\n')
        a = input()

        os.system('cls')

        if a == '1':
            self.verificar_conta()
            
        elif a == '2':
            n = input('Nome: ')
            ncont = input('Número da conta: ')
            saldo = int(input('Saldo conta: '))
            ContaBancaria(ncont, n, saldo)

        elif a == '3':
            deposito = int(input('Quanto deseja depositar?\n'))
            self.depositar(deposito)

        elif a == '4':
            saque = int(input('Quanto deseja sacar?\n'))
            self.sacar(saque)

    def proxima_acao(self):
        a = input('Deseja voltar ao menu?[s/n]\n')
        if a == 's':
            os.system('cls')
            self.menu()

# Crie uma instância da classe ContaBancaria para iniciar o menu
conta_inicial = ContaBancaria("0000", "admin", 0)
