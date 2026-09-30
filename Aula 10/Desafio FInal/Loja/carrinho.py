class Carrinho:
    def __init__(self, produtos=[]):
        self.produtos = produtos
    
    def adicionar(self, produto):
        print(f"Adicionando {produto.nome} de valor R${produto.preco} ao carrinho.")
        self.produtos.append(produto)
    
    def ver_carrinho(self):
        i = 1
        if len(self.produtos) > 0:
            print("Lista de Itens no Carrinho:")
            for item in self.produtos:
                print(f"{i}: {item.nome} / R${item.preco}")
                i += 1
        else:
            print("Carrinho Vazio")