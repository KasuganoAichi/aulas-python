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

class Sirene:
    def __init__(self):
        pass

    def falar(self):
            return f"Sirene emite sons de sirene."

a = Cachorro("Brutus")
b = Gato("Pixie")
c = Pato("Randal")
d = Sirene()

animais = [a, b, c, d]

for animal in animais:
     print(animal.falar())