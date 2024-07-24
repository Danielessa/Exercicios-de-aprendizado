import os

class ContaBancaria:
    contas = []
    def __init__(self, N_conta, titular, saldo):
        self.N_conta = N_conta
        self.titular = titular
        self.saldo = saldo
        self.contas.append(self)
        proxima_acao()

    def encontrar_conta():
        titular = input('Quem é o titular da conta?\n')
        for usuario in ContaBancaria.contas:
            if usuario.titular == titular:
                return usuario


    def verificar_conta():

        usuario = ContaBancaria.encontrar_conta()
        
        print(f'N_conta: {usuario.N_conta}')
        print(f'Titular: {usuario.titular}')
        print(f'Saldo: {usuario.saldo}')
        
        proxima_acao()
    
    def depositar(v_deposito):
        usuario = ContaBancaria.encontrar_conta()

        print(f'Foi depositado R$ {v_deposito} na sua conta')
        usuario.saldo += v_deposito
        proxima_acao()

    def sacar(v_saque):
        usuario = ContaBancaria.encontrar_conta()

        print(f'Foi sacado R$ {v_saque} da sua conta')
        usuario.saldo -= v_saque
        proxima_acao()

def menu():
    print('MENU\n')
    print('1 - Verificar conta')
    print('2 - Cadastrar conta')
    print('3 - Deposito')
    print('4 - Saque\n')
    a = input()

    os.system('cls')

    if a == '1':
        ContaBancaria.verificar_conta()
        
    elif a == '2':
        n = input('Nome: ')
        ncont = input('Número da conta: ')
        saldo = int(input('Saldo conta: '))
        usuario = ContaBancaria(ncont, n, saldo)

    elif a == '3':
        deposito = int(input('Quanto deseja depositar?\n'))
        ContaBancaria.depositar(deposito)

    elif a == '4':
        saque = int(input('Quanto deseja sacar?\n'))
        ContaBancaria.sacar(saque)

def proxima_acao():
    a = input('Deseja voltar ao menu?[s/n]\n')
    if a == 's':
        os.system('cls')
        menu()


menu()




