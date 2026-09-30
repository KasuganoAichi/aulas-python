compras = ["arroz", "feijão", "macarrão", "carne", "frango"]


produto = input("Informe produto que deseja conferir: ")
if produto in compras:
    print(f"{produto} está na lista.")
else:
    print(f"{produto} não está na lista.")