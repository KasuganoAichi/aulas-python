class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def aumentar_salario(self, valor):
        if valor < 0:
            print("O aumento de salário não pode ser negativo.")
            return
        self.__salario += valor

