class Conta_Bancaria():
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido. O depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Valor inválido. O saque deve ser positivo e não pode exceder o saldo.")

    def get_saldo(self):
        return self.__saldo