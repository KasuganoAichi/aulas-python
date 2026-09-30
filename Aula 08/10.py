class Cofre:
    def __init__(self, senha, conteudo):
        self.__senha = senha
        self.__conteudo = conteudo

    def abrir(self, senha):
        if senha == self.__senha:
            return self.__conteudo
        else:
            print("Senha incorreta. Acesso negado.")
            return None

    def guardar(self, senha, novo_conteudo):
        if senha == self.__senha:
            self.__conteudo = novo_conteudo
            print("Conteúdo atualizado com sucesso.")
        else:
            print("Senha incorreta. Não foi possível atualizar o conteúdo.")


cofre = Cofre("1234", "Segredo do Cofre")

cofre.abrir("2")
cofre.abrir("1234")
cofre.guardar("2", "Novo Segredo")
cofre.guardar("1234", "Novo Segredo")