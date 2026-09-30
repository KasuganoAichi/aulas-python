numlist = [1, 2, 3, 4, 5, 6, 7, 8 ]
pares = int(0)

for n in numlist:
    if n % 2 == 0:
        pares += 1

print(f"QTD de pares: {pares}")