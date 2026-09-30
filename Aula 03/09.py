padaria = [{'nome' : 'leite', 'preco' : 5.00}, {'nome' : 'mussarela', 'preco' : 3.5}, {'nome' :'presunto', 'preco' : 4.5}]

for produto in padaria:
    print(f"{produto['nome']} : {produto['preco']}")