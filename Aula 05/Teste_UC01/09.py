n = int(input("Digite um número inteiro: "))
soma =int(0)

for i in range(1, n):
    soma += i

print(f"\nA soma dos números de 1 a {n} é: {soma}")