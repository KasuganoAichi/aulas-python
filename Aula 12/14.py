produtos = {"caneta" : 50, "caderno" : 20, "mochila" : 10, "borracha" : 35}

buscar = input("Informe qual produto deseja buscar no estoque: ").lower()
try:
    print(f"Quantidade em estoque: {produtos[buscar]}")
except KeyError:
    print("Produto não encontrado.")