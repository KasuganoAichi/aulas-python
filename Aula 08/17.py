class Relogio:
    def __init__(self, hora=0):
        self.hora = hora

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, valor):
        if not 0 <= valor < 24:
            print("A hora deve estar entre 0 e 23. Não foi realizada a alteração")
            return
        self._hora = valor