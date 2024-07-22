class ContaBancaria:
    contas = []
    def __init__(self, N_conta, titular, saldo):
        self.N_conta = N_conta
        self.titular = titular
        self.saldo = saldo
        self.contas.append(self)

    def verificar_conta():
        print(f'N_conta: {ContaBancaria.N_conta}')
        print(f'Titular: {ContaBancaria.titular}')
        print(f'Saldo: {ContaBancaria.saldo}')

    
    def depositar(self, v_deposito):
        print(f'Foi depositado R$ {v_deposito} na sua conta')
        self.saldo += v_deposito

    def sacar(self, v_saque):
        print(f'Foi sacado R$ {v_saque} da sua conta')
        self.saldo -= v_saque


    def menu(self):
        print('MENU\n')
        print('1 - Verificar conta')
        print('2 - Cadastrar conta')
        print('3 - Deposito')
        print('4 - Saque\n')
        a = input()

        if a == '1':
            self.verificar_conta()
        
        elif a == '2':
            n = input('Nome: ')
            ncont = input('Número da conta: ')
            saldo = int(input('Saldo conta: '))

        elif a == '3':
            self.depositar()

        elif a == '4':
            self.depositar()

ContaBancaria.menu()




