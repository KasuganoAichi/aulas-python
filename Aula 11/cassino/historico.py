class Historico:
    def __init__(self, resultados=[]):
        self.resultados = resultados

    def registrar(self, valor):
        self.resultados.append(valor)
        return

    def maior(self):
        maior = 0
        for valor in self.resultados:
            if valor > maior:
                maior = valor
        return maior if self.resultados else "Histórico vazio"

    def media(self):
        i = 0
        media = 0
        for valor in self.resultados:
            media += valor
            i += 1
        return media / i if self.resultados else "Histórico vazio"

if __name__ == "__main__":
    print("Está em Histórico")