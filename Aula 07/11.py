class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

print(f"Título: {livro.titulo}")
