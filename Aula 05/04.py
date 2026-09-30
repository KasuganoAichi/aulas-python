import os

if os.path.exists("frutas.txt"):
    with open("frutas.txt", "r")as file:
        for line in file:
            print(line.strip())