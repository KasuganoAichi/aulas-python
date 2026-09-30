class Aluno:
    def __init__ (self,nome,nota,curso):
        self.nome = nome
        self.nota = nota
        self.curso = curso

    def situacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"

    def __str__(self): #m etodo especial
        #como o aluno aparece como texto na Listbox
        return f"{self.nome} - Curso: {self.curso} - Nota: {self.nota} ({self.situacao()})"