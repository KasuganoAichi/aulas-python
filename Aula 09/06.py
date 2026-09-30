class Vendedor:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self, comissao):
        return self.salario + comissao

class Gerente:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self, bonus):
        return self.salario + bonus

v = Vendedor("Leonardo", 1750.00)
g = Gerente("Leandro", 2500.00)

loja = [v, g]

for funcionario in loja:
    print(f"Funcionario: {funcionario.nome}\nSalário: R${funcionario.calcular_salario(350)}")