import os

if os.path.exists("dados_secretos.txt"):
    with open("dados_secretos.txt", "r") as file:
        print(file.read())
else:
    print("Arquivo inexistente")