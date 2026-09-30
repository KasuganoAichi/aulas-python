class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self._nota = 0
        self.nota = nota  # valida no setter

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if not 0 <= valor <= 10:
            print("A nota deve estar entre 0 e 10.")
            return
        self._nota = valor


aluno1 = Aluno("João", -2)
print(aluno1.nome, aluno1.nota)