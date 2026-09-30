n = int(0)
positivos = int(0)
negativos = int(0)
zerados = int(0)

for i in range(1, 6):
    n = int(input(f"Digite o {i}º número: "))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        zerados += 1

print(f"\nTotal de Positivos: {positivos}")
print(f"\nTotal de Positivos: {negativos}")
print(f"\nTotal de Positivos: {zerados}")
