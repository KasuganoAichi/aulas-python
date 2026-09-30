class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco

laranja = Produto("Laranja", 2.5)

print(laranja.preco)