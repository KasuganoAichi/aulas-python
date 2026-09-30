def real_para_dolar(valor):
    return valor / 5.10

def dolar_para_real(valor):
    return valor * 5.10 if valor > 0 else "Valor não pode ser 0."

def real_para_euro(valor):
    return valor / 5.92


if __name__ == "__main__":
    print("Está na main")