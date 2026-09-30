base = input("Informe base do triângulo: ")
altura = input("Informe altura do triângulo: ")

try:
    base = float(base)
    altura = float(altura)
except ValueError:
    print("Todos os dados informados devem ser valores númericos.")
else:
    area = base * altura
    print(f"Área: {area}")
finally:
    print("Operação de cálculo concluída.")