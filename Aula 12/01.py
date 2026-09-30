entrada = input("Digite um número: ")

try:
    entrada = int(entrada)
    print(f"Número digitado: {entrada}")
except ValueError:
    print("Valor inválido")