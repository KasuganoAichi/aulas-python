with open("teste.txt", "w")as file:
    file.write("Estou aprendendo arquivos!")

with open("teste.txt", "r")as file:
    print(file.read())