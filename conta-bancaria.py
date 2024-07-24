import os

class ContaBancaria:
    contas = []
    def __init__(self, N_conta, titular, saldo):
        self.N_conta = N_conta
        self.titular = titular
        self.saldo = saldo
        self.contas.append(self)
        proxima_acao()

    def verificar_conta():
        titular = input('Quem é o titular da conta?\n')
        
        for usuario in ContaBancaria.contas:
            if usuario.titular == titular:
                print(f'N_conta: {usuario.N_conta}')
                print(f'Titular: {usuario.titular}')
                print(f'Saldo: {usuario.saldo}')
        
        proxima_acao()
    
    def depositar(self, v_deposito):
        print(f'Foi depositado R$ {v_deposito} na sua conta')
        self.saldo += v_deposito
        proxima_acao()

    def sacar(self, v_saque):
        print(f'Foi sacado R$ {v_saque} da sua conta')
        self.saldo -= v_saque
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
        ContaBancaria.depositar()

    elif a == '4':
        ContaBancaria.depositar()

def proxima_acao():
    a = input('Deseja voltar ao menu?[s/n]\n')
    if a == 's':
        os.system('cls')
        menu()


menu()




