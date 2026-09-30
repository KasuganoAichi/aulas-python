class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, inimigo):
        if self.vida <= 0:
            print(f"{self.nome} não pode atacar, pois está derrotado!")
            return
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} já está derrotado!")
            return
        inimigo.vida -= self.forca
        if inimigo.vida <= 0:
            inimigo.vida = 0
            print(f"{self.nome} atacou {inimigo.nome} causando {self.forca} de dano!")
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{self.nome} atacou {inimigo.nome} causando {self.forca} de dano!")

agumon = Personagem("Agumon", 100, 20)
gabumon = Personagem("Gabumon", 80, 15)

agumon.atacar(gabumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
agumon.atacar(gabumon)
agumon.atacar(gabumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
gabumon.atacar(agumon)
agumon.atacar(gabumon)