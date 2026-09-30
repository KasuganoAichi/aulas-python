class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
    def listar_itens(self):
        return [item for item in self.itens]


carrinho = CarrinhoDeCompras()
carrinho.adicionar_item("Arroz")
carrinho.adicionar_item("Feijão")
carrinho.adicionar_item("Massa")
carrinho.adicionar_item("Frango")
carrinho.adicionar_item("Tomate")
print(*carrinho.listar_itens())
carrinho.remover_item("Massa")
carrinho.remover_item("Massa")
print(*carrinho.listar_itens())