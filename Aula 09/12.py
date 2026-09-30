class Guerreiro:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} ataca com sua Espada.")

class Mago:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} ataca com Magia.")

class Arqueiro:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} ataca com seu Arco.")

a = Arqueiro("Legolas")
g = Guerreiro("Gimli")
m = Mago("Gandalf")

fichas = [a, g, m]

for ficha in fichas:
    ficha.atacar()

