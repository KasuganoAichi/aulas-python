total = input("Informe valor total da conta: ")
pagantes = input("Informe número pessoas pagantes: ")

try:
    total = float(total)
    pagantes = int(pagantes)
    total = total / pagantes
    print(f"Valor dividido: {total}")
except ZeroDivisionError:
    print("Número de pessoas não pode ser zero.")
except ValueError:
    print("Valores informados devem ser numéricos.")