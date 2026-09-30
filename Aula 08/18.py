class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

        @property
        def titulo(self):
            return self._titulo

        @property
        def autor(self):
            return self._autor

meu_livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")
print(meu_livro._titulo)
meu_livro.titulo = "O Hobbit" 
print(meu_livro._titulo)