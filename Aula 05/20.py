import os
import csv

def menu():
    print("1 - Cadastrar Filme.")
    print("2 - Listar Filmes.")
    print("3 - Encerrar.")

def cadastrarfilme(filme, ano):
    if os.path.exists("catalogo.csv"):
        with open("catalogo.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([filme, ano])
    else:
        with open("catalogo.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["titulo", "ano"])
            writer.writerow([filme, ano])

def listarfilme():
    if os.path.exists("catalogo.csv"):
        with open("catalogo.csv", "r") as file:
            reader = csv.reader(file)
            for line in reader:
                print(*line)
    else:
        print("Arquivo inexistente")

filme = ""
ano = ""
option = int()

while True:
    menu()
    option = int(input("Informe o número da opção desejada: "))
    if option == 1:
        filme = input("Informe nome do filme: ")
        ano = input("Informe ano de lançamento: ")
        cadastrarfilme(filme, ano)
    elif option == 2:
        listarfilme()
    elif option == 3:
        print("Encerrando programa.")
        break
    else:
        print("Opção desconhecida, favor informar uma opção válida.\n\n")
