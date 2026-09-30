nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
cidade = input("Informe sua cidade: ")

habitante = {}
habitante['nome'] = nome
habitante['idade'] = idade
habitante['cidade'] = cidade

print(f"Olá {habitante['nome']}, você tem {habitante['idade']} e mora em {habitante['cidade']}")