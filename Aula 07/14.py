class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

produto1 = Produto("Booster CORI", 35.00)
produto2 = Produto("Booster STRIXHEAVEN", 45.00)
produto3 = Produto("Booster MEG", 15.00)

print(f"{produto1.nome}, R${produto1.preco:.2f}")
print(f"{produto2.nome}, R${produto2.preco:.2f}")
print(f"{produto3.nome}, R${produto3.preco:.2f}")

produto1.aplicar_desconto(20)
print(f"{produto1.nome}, R${produto1.preco:.2f}")