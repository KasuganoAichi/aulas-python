class Televisao:
    def __init__(self):
        pass

    def ligar(self):
        print("A TV está ligada.")

class Radio:
    def __init__(self):
        pass

    def ligar(self):
        print("O Radio está ligado.")

class Lampada:
    def __init__(self):
        pass

    def ligar(self):
        print("A Lampada está ligada.")

t = Televisao()
r = Radio()
l = Lampada()

eletros = [t, r, l]

for eletro in eletros:
    eletro.ligar()