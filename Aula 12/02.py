n1 = int(input("Digite primeiro número: "))
n2 = int(input("Digite segundo número: "))

try:
    print(f"Resultado: {n1 / n2}")
except ZeroDivisionError:
    print("Não é possível dividir por zero (0)")