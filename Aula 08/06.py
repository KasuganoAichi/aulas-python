class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print("Preço não pode ser negativo")
            return
        self._preco = valor
    

laranja = Produto("Laranja", 2.5)

laranja.preco = 3.0
laranja.preco = -5.2

print(laranja.preco)