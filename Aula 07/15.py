class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo1 = Retangulo(5, 10)
print(f"Largura: {retangulo1.largura}, Altura: {retangulo1.altura}")
print(f"Área: {retangulo1.calcular_area()}")
print(f"Perímetro: {retangulo1.calcular_perimetro()}")