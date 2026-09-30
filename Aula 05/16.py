convidados = ["Ana", "Carlos", "Beatriz", "Daniel"]

with open("lista_festa.txt", "w")as file:
    for person in convidados:
        file.write(person + "\n")