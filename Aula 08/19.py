class Usuario:
    def __init__(self, usuario, senha):
        self._usuario = usuario
        self.senha = senha

    @property
    def usuario(self):
        return self._usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
            return
        self._senha = valor


user1 = Usuario("usuario1", "senha123")
print(user1.senha)
user1.senha = "nova"
print(user1.senha)