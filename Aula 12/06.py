try:
    n = int(input("Informe um número: "))
except ValueError:
    print("Entrada deve ser um número.")
else:
    print(f"Número válido: {n}")