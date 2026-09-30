import os

def menu():
    print("1 - Inserir nova anotação.")
    print("2 - Mostrar anotações.")
    print("3 - Encerrar.")

def cadastraranotacao(anotacao):
    if os.path.exists("notas.txt"):
        with open("notas.txt", "a") as file:
            file.write(anotacao)
            file.write("\n")
    else:
        with open("notas.txt", "w") as file:
            file.write(anotacao)
            file.write("\n")

def listaranotacoes():
    if os.path.exists("notas.txt"):
        with open("notas.txt", "r") as file:
            for line in file:
                print(line.strip())
    else:
        print("Arquivo inexistente")

anotacao = ""
option = int()

while True:
    menu()
    option = int(input("Informe o número da opção desejada: "))
    if option == 1:
        anotacao = input("Informe nova anotação: ")
        cadastraranotacao(anotacao)
    elif option == 2:
        listaranotacoes()
    elif option == 3:
        print("Encerrando programa.")
        break
    else:
        print("Opção desconhecida, favor informar uma opção válida.\n\n")
