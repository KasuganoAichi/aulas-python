padaria = {'pão' : 2.5, 'leite' : 5.00, 'mussarela' : 3.5, 'presunto' : 4.5}

produto = input("Qual produto deseja consultar? ")

if padaria.get(produto) != None:
    print(f"{produto} custa R${padaria[produto]}")
else:
    print(f"{produto} não está disponível")