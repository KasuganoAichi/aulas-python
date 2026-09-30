class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor <= 0:
            print("O raio deve ser maior que zero.")
            return
        self._raio = valor

    @property
    def area(self):
        return 3.14159 * self.raio ** 2


c = Circulo(3)
print(f"Raio: {c.raio}")
print(f"Área: {c.area:.2f}")