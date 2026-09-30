class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10
        print(f"Velocidade atual: {self.velocidade}")

    def frear(self):
        if self.velocidade == 0:
            print("Carro parado, não há como reduzir a velocidade.")
        else:
            self.velocidade -= 10
            print(f"Velocidade atual: {self.velocidade}")

carro1 = Carro("Renault", "Onix")
carro1.frear()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()

    