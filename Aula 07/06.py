class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depositado: R${valor:.2f}. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Sacado: R${valor:.2f}. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

conta1 = ContaBancaria("Leonardo", 120)

conta1.consultar_saldo()
conta1.depositar(50)
conta1.sacar(30)
conta1.sacar(200)