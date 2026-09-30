with open("pontuacoes.csv", "r") as file:
    next(file)
    for linha in file:
        name, point = linha.strip().split(",")
        print(f"O jogador {name} fez {point} pontos.")