class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura        

    def area(self):
        return self.base * self.altura

def apresentar_area(forma):
    area = forma.area()
    print(f"A área é: {area}")

q = Quadrado(5)
t = Triangulo(5, 10)

areas = [q, t]

for area in areas:
    apresentar_area(area)
