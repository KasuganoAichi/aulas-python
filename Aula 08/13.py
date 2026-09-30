class Carro:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self._velocidade = 0
        self.velocidade = velocidade

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor < 0:
            print("A velocidade não pode ser negativa.")
            return
        self._velocidade = valor


carro1 = Carro("Toyota", 150)
print(carro1.velocidade)
carro1.velocidade = -50
print(carro1.velocidade)
