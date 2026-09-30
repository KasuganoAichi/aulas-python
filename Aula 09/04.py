class PagamentoCartao:
    def __init__(self):
        pass

    def processar(self, valor):
        return f"Realizando pagamento com Cartao no valor de {valor}."

class PagamentoPix:
    def __init__(self):
        pass

    def processar(self, valor):
        return f"Gerando QR Code de Pix no valor de {valor}."

def pagar(forma, valor):
    return forma.processar(valor)

p = PagamentoCartao()
p2 = PagamentoPix()

print(pagar(p, 500.00))
print(pagar(p2, 250.50))