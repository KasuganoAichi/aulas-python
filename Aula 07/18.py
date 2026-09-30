class Mascote:
    def __init__(self, nome, fome=50, energia=50):
        self.nome = nome
        self.fome = fome
        self.energia = energia

    def comer(self):
        if self.fome < 100 and self.energia > 0:
            self.fome += 10
            if self.fome > 100:
                self.fome = 100
            self.energia -= 5
            if self.energia < 0:
                self.energia = 0
            print(f"{self.nome} está comendo. Fome: {self.fome}")
        else:
            print(f"{self.nome} não está com fome.")

    def dormir(self):
        if self.energia < 100 and self.fome > 0:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
            self.fome -= 10
            if self.fome < 0:
                self.fome = 0
            print(f"{self.nome} está dormindo. Energia: {self.energia}")
        else:
            print(f"{self.nome} não está cansado.")

    def status(self):
        print(f"{self.nome} - Fome: {self.fome}, Energia: {self.energia}")

pet = Mascote("Fido")
pet.status()
pet.comer()
pet.comer()
pet.comer()
pet.comer()
pet.comer()
pet.comer()
pet.dormir()
pet.dormir()
pet.dormir()
pet.dormir()
pet.dormir()
pet.dormir()
pet.dormir()
pet.dormir()
