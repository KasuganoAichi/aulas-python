class Termometro:
    def __init__(self, temperatura=0):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273:
            print("Temperatura não pode ser menor que -273°C")
            return
        self._temperatura = valor

temp = Termometro(25)
temp.temperatura = -300
temp.temperatura = 20

print(temp.temperatura)