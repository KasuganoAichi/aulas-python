class Carro:
    def __init__(self, marca, velocidade):
        self.marca = marca
        self._velocidade = 0
        self.velocidade = velocidade

    @property
    def get_velocidade(self):
        return self._velocidade

carro1 = Carro("Toyota", 150)
print(carro1.get_velocidade)