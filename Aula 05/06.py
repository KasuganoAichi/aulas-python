import os

if os.path.exists("frutas.txt"):
    with open("frutas.txt", "r")as file:
        linhas = file.readlines()
        print(len(linhas))