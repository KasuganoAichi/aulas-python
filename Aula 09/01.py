class Pato:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"{self.nome} diz: Quack Quack"

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
            return f"{self.nome} diz: Au Au"

class Gato:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
            return f"{self.nome} diz: Miau Miau"

a = Cachorro("Brutus")
b = Gato("Pixie")
c = Pato("Randal")

animais = [a, b, c]

for animal in animais:
     print(animal.falar())