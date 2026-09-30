class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print("Woof! Woof!")

dog = Cachorro("Brutus", "Pastor Alemão")

print(f"{dog.nome}:")
dog.latir()