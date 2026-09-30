class Circulo:
    def __init__(self):
        pass

    def desenhar(self):
        print("Desenhando um Círculo.")

class Retangulo:
    def __init__(self):
        pass

    def desenhar(self):
        print("Desenhando um Retângulo.")

def renderizar(forma):
    forma.desenhar()

c = Circulo()
r = Retangulo()

renderizar(c)
renderizar(r)