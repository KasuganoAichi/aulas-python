class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = pessoa("Leonardo", 28)
pessoa2 = pessoa("Lucas", 25)

print(f"{pessoa1.nome}, {pessoa1.idade} anos")
print(f"{pessoa2.nome}, {pessoa2.idade} anos")