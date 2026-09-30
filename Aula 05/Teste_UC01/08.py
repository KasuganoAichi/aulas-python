n = int(input("Informe número para ser calculado a tabuada: "))

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")