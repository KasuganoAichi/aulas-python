from Loja.produto import Produto
from Loja.carrinho import Carrinho

c = Carrinho()
c.ver_carrinho()
p1 = Produto("Laranja", 4.50)
p2 = Produto("Bergamota", 7.50)
p3 = Produto("Limão", 11.50)

c.adicionar(p1)
c.adicionar(p2)
c.adicionar(p3)
print("\n\n")

c.ver_carrinho()