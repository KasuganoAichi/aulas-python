import os
import csv

catalogo = []

def criar_filme(titulo, diretor, ano, catalogo):
    catalogo.append({"Titulo" : titulo, "Diretor" : diretor, "Ano" : ano})
    return catalogo

def mostrar_filme(filme):
    if filme:
        print(f"Título : {filme["Titulo"]} | Diretor: {filme["Diretor"]} | Ano : {filme["Ano"]}")
    else:
        print("Filme não encontrado.")

def listar_filmes(catalogo):
    if len(catalogo) == 0:
        print("Não há filmes cadastrados.")
        return
    else:
        catalogo_ordenado = sorted(catalogo, key=lambda x: x["Titulo"])
        for filme in catalogo_ordenado:
            mostrar_filme(filme)

def busca_por_diretor(catalogo, nome_diretor):
    if len(catalogo) == 0:
        print("Não há filmes cadastrados.")
        return
    else:
        for filme in catalogo:
            if filme["Diretor"].lower() == nome_diretor.lower():
                mostrar_filme(filme)

def atualizar_ano(catalogo, titulo_buscado, ano_novo):
    if len(catalogo) == 0:
            print("Não há filmes cadastrados.")
            return catalogo
    else:
        for filme in catalogo:
            if filme["Titulo"].lower() == titulo_buscado.lower():
                filme["Ano"] = ano_novo
                print("Alteração de ano lançamento concluída.")
                return catalogo
        print("Filme não encontrado")
        return catalogo

def salvar_catalogo(catalogo):
    arquivo = "catalogo_filmes.csv"
    with open(arquivo, "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Titulo", "Diretor", "Ano"])
        for filme in catalogo:
            escritor.writerow([filme["Titulo"], filme["Diretor"], filme["Ano"]])

def carregar_catalogo():
    arquivo = "catalogo_filmes.csv"
    catalogo = []
    if os.path.exists(arquivo):
        with open(arquivo, "r", newline="") as arquivo:
            next(csv.reader(arquivo))
            for linha in csv.reader(arquivo):
                catalogo.append({"Titulo" : linha[0], "Diretor" : linha[1], "Ano" : linha[2]})
    return catalogo

def remover_filme(catalogo, titulo_excluir):
    if len(catalogo) == 0:
        print("Não há filmes cadastrados.")
        return catalogo
    for filme in catalogo:
        if filme["Titulo"].lower() == titulo_excluir.lower():
            catalogo.remove(filme)
            print("Filme removido!")
            return catalogo
    print("Filme não encontrado.")
    return catalogo


def main():
    catalogo = carregar_catalogo()
    diretor = ""
    titulo = ""
    ano = ""
    opcao = ""
    while True:
        print(f" == BIBLIOTECA DE FILMES== ")
        print("1 - Cadastrar Filme")
        print("2 - Listar Filmes")
        print("3 - Buscar por Diretor")
        print("4 - Atualizar Ano")
        print("5 - Remover")
        print("6 - Sair")
        opcao = input("Informe opção que seja executar: ")    
        if opcao == "1":
            titulo = input("Informe Título do Filme: ")
            diretor = input("Informe Diretor do Filme: ")
            ano = input("Informe Ano do Filme: ")
            salvar_catalogo(catalogo = criar_filme(titulo, diretor, ano, catalogo))
        elif opcao == "2":
            listar_filmes(catalogo)
        elif opcao == "3":
            diretor = input("Informe nome do Direto cujos filmes deseja descobrir: ")
            busca_por_diretor(catalogo, diretor)
        elif opcao == "4":
            titulo = input("Informe nome do filme que deseja atualizar o ano: ")
            ano = input("Informe ano atualizado: ")
            salvar_catalogo(catalogo = atualizar_ano(catalogo, titulo, ano))
        elif opcao == "5":
            titulo =  input("Informe titulo do filme a ser excluído: ")
            salvar_catalogo(catalogo = remover_filme(catalogo, titulo))
        elif opcao == "6":
            print("Programa encerrado")
            break
        else:
            print("Opção desconhecida, informe novamente.")


#Inicio do Programa
main()