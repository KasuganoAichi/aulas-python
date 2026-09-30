class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0 and idade <= 120:
            self.__idade = idade
        else:
            print("Idade inválida. A idade não pode ser negativa.")

pessoa = Pessoa("Alice", 30)
print(pessoa.get_idade())
pessoa.set_idade(35)
print(pessoa.get_idade())