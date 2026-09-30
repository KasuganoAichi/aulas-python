class Livro:
    def __init__(self):
        pass

    def calcular_preco_final(self, preco_base):
        return preco_base - (preco_base * 0.1)

class Eletronico:
    def __init__(self):
        pass

    def calcular_preco_final(self, preco_base):
        return preco_base - (preco_base * 0.05)

l = Livro()
e = Eletronico()

vendas = [l, e]

for item in vendas:
    print(f"Valor Final do Item: {item.calcular_preco_final(100)}")
