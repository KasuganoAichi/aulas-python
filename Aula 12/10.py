def sacar(saldo, valor):
    if valor < 0:
        raise ValueError("Valor de Saque não pode ser negativo.")
    elif valor > saldo:
        raise ValueError("Saldo insuficiente.")
    return saldo - valor

while True:
    saldo = input("Informe valor de saldo: ")
    valor = input("Informe valor do saque: ")
    try:
        saldo = float(saldo)
        valor = float(valor)
        try:
            novosaldo = sacar(saldo, valor)
            print(f"Saldo restante após o saque: {sacar(saldo, valor):.2f}")
            break
        except ValueError as erro:
            print(f"\n {erro}")
    except ValueError:
        print("\n Informe apenas valores numéricos.")
    