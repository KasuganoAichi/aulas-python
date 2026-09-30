class Email:
    def __init__(self):
        pass

    def enviar(self, mensagem):
        return f"Enviando {mensagem} por email."

class SMS:
    def __init__(self):
        pass

    def enviar(self, mensagem):
        return f"Enviando {mensagem} por SMS."

class Push:
    def __init__(self):
        pass

    def enviar(self, mensagem):
        return f"Enviando {mensagem} por Push."

def notificar_todos(canais, mensagem):
    for canal in canais:
        print(canal.enviar(mensagem))

e = Email()
s = SMS()
p = Push()

notificar_todos([e, s, p], "LOL")