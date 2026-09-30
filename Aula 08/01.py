class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    def get_idade(self):
        return self.__idade

pessoa = Pessoa("Alice", 30)
print(pessoa.get_idade())