n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O maior número é: {n1}")
elif n2 > n3:
    print(f"O maior número é: {n2}")
else:
    print(f"O maior número é: {n3}")