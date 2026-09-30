nomes = ["Alan", "Danti", "Guilherme", "Leonardo", "Lucas"]

with open("nomes.txt", "w")as file:
    for item in nomes:
        file.write(item)
        file.write("\n")
with open("nomes.txt", "r")as file:
    print(file.read().strip())