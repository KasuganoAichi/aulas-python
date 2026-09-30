import math

def raiz_quadrada(n):
    if n < 0:
        raise ValueError("Número negativo não tem raiz real.")
    return math.sqrt(n)

n = int(input("Digite um número: "))
print(f"Raíz quadrada de {n} = {raiz_quadrada(n)}")