class Aluno:
    def __init__(self,nome,n1,n2,n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def media(self):
        print(f"Media do aluno: {(self.n1 + self.n2 + self.n3) / 3}")

aluno1 = Aluno("Leonardo", 8, 7, 9)
aluno1.media()