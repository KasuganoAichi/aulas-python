namelist = []
newname = ""

for i in range(1, 6):
    newname = input("Digite um nome: ")
    namelist.append(newname)

namelist.sort()
print(f"Lista de nomes: {namelist}")