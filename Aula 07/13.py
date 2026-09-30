class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

pessoa.idade = 27

print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")