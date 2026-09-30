class Brasileiro:
    def __init__(self):
        pass

    def saudar(self):
        print("Olá")

class Espanhol:
    def __init__(self):
        pass

    def saudar(self):
        print("Hola")

class Ingles:
    def __init__(self):
        pass

    def saudar(self):
        print("Hello")

b = Brasileiro()
e = Espanhol()
i = Ingles()

lista = [b, e, i]

for item in lista:
    item.saudar()