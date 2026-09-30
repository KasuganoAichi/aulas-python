def eh_par(n):
    return n % 2 == 0

x = int(input("Informe um número inteiro: "))
if eh_par(x):
    print("O número é par")
else:
    print("O número é ímpar")