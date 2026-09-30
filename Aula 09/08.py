class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f"Um Carro {self.modelo} da {self.marca}.")

class Moto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f"Uma Moto {self.modelo} da {self.marca}.")

class Caminhao:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        print(f"Um Caminhão {self.modelo} da {self.marca}.")

c = Carro("Ford", "Punto")
t = Caminhao("Toyota", "Corolla")
m = Moto("Hyundai", "Miraidon")

veiculos = [c, t, m]

for veiculo in veiculos:
    veiculo.descrever()