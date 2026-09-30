digitados = int(0)
n = float(0)
total = float(0)
maior = float(0)

while True:
    n = float(input("Digite um número: "))
    total += n
    if n > maior:
        maior = n
    if n == 0:
        print("\nPrograma encerrado.")
        print(f"\nTotal de números digitados antes do zero: {digitados}")
        print(f"\nSoma dos números digitados: {total}")
        print(f"\nMaior número digitado: {maior}")
        break
    digitados += 1