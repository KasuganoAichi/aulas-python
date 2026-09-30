class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

produto1 = Produto("Booster CORI", 35.00)

print(f"{produto1.nome}, R${produto1.preco:.2f}")
print("Aplicando desconto de 10%...")
produto1.aplicar_desconto(10)

print(f"{produto1.nome}, R${produto1.preco:.2f}")