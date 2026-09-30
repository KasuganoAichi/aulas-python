newmovie = input("Informe nome do novo filme: ") + "\n"

with open("meus_filmes.txt", "a")as file:
    file.write(newmovie)