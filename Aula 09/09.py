class Violao:
    def __init__(self):
        pass

    def tocar(self):
        print("*Sons de Violão*")

class Bateria:
    def __init__(self):
        pass

    def tocar(self):
        print("*Sons de Bateria*")

class Piano:
    def __init__(self):
        pass

    def tocar(self):
        print("*Sons de Piano*")

def banda(instrumentos):
    for i in instrumentos:
        i.tocar()

v = Violao()
p = Piano()
b = Bateria()

banda([v, b, p])