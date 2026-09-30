with open("lembretes.txt", "r") as file:
    for line in file:
        print(file.read().strip())