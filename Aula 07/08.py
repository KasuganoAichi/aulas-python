class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível na biblioteca.")

livro1 = Livro("A Revolução dos Bichos", "George Orwell")
livro2 = Livro("1984", "George Orwell")
livro1.emprestar()
livro1.emprestar()
livro1.devolver()
livro2.emprestar()
livro2.devolver()
livro2.devolver()  