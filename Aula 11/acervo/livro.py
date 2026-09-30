class Livro:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    def eh_recente(self):
        return True if self.ano > 2015 else False

