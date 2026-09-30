class Aluno:
    def __init__(self,nome,n1,n2,n3):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def media(self):
        print(f"Media do aluno: {(self.n1 + self.n2 + self.n3) / 3}")

turma = []
turma.append(Aluno("João", 7, 8, 9))
turma.append(Aluno("Maria", 6, 5, 7))
turma.append(Aluno("Pedro", 9, 8, 10))
turma.append(Aluno("Ana", 5, 6, 7))
turma.append(Aluno("Lucas", 8, 9, 10))

for aluno in turma:
    print(f"Aluno: {aluno.nome}")
    aluno.media()