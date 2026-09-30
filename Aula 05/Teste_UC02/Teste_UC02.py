import csv, os

alunos = []
print(alunos)
aprovados = int(0)
reprovados = int(0)

def salvar_alunos(alunos):
    arquivo = "alunos2.csv"
    with open(arquivo, "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Nota", "Curso"])
        for aluno in alunos:
            escritor.writerow([aluno["Nome"], aluno["Nota"], aluno["Curso"]])

def carregar_alunos():
    arquivo = "alunos2.csv"
    alunos = []
    if os.path.exists(arquivo):
        with open(arquivo, "r", newline="") as arquivo:
            next(csv.reader(arquivo))
            for linha in csv.reader(arquivo):
                alunos.append({"Nome" : linha[0], "Nota" : float(linha[1]), "Curso" : linha[2]})
    return alunos

def validanota():
    nota = float(input("Nota do Aluno: "))
    while nota <= 0 or nota > 10:
        print("Valor da nota inválido, informe novamente.")
        nota = float(input("Nota do Aluno: "))
    return nota

def cadastrar(alunos):
    nome = input("Nome do Aluno: ")
    nota = validanota()
    curso = input("Nome do Curso: ")
    alunos.append({"Nome" : nome, "Nota" : nota, "Curso" : curso})
    print("Aluno cadastrado com sucesso!")
    return alunos

def listar(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    alunosordenados = sorted(alunos, key=lambda x: x["Nome"])
    print("\n ## LISTA DE ALUNOS ##")
    for aluno in alunosordenados:
        if aluno ["Nota"] >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        print(f"{aluno['Nome']} - Nota: {aluno['Nota']} - {situacao} - Curso: {aluno['Curso']}")

def buscar(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    termo = input("Buscar qual nome? ")
    encontrados = 0
    for aluno in alunos:
        if termo.lower() == aluno["Nome"].lower():
            print(f"Encontrado: {aluno['Nome']} - Nota: {aluno['Nota']} - Curso: {aluno['Curso']}")
            encontrados += 1
    if encontrados == 0:
        print(f"Não há aluno de nome {termo} cadastrado.")

def remover(alunos):
    if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
            return alunos
    nome = input("Nome para remover: ")
    for aluno in alunos:
        if aluno["Nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print("Aluno removido!")
            return alunos
    print("Aluno não encontrado.")
    return alunos

def mediageral(alunos):
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        return
    return sum(float(aluno["Nota"]) for aluno in alunos) / len(alunos)

def qtdaprovados(alunos):
    aprovados = int(0)
    reprovados = int(0)
    if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
            return
    for aluno in alunos:
        if aluno ["Nota"] >= 6:
            aprovados += 1
        else:
            reprovados += 1
    print(f"\nTotal de alunos aprovados: {aprovados}")
    print(f"\nTotal de alunos reprovados: {reprovados}")

def editarnota(alunos):
    if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
            return
    nome = input("Nome para editar: ")
    for aluno in alunos:
        if aluno["Nome"].lower() == nome.lower():
            nota = validanota()
            aluno["Nota"] = nota
            return alunos
    print("Aluno não encontrado.")
    return alunos

def comparamedia(alunos):
    if  len(alunos) == 0 : 
        print("Nenhum aluno cadastrado.")
        return
    aluno_melhor = max(alunos, key=lambda x: float(x["Nota"]))
    aluno_pior = min(alunos, key=lambda x: float(x["Nota"]))
    print(f"\n{aluno_melhor['Nome']} possui a maior nota, {aluno_melhor['Nota']}")
    print(f"{aluno_pior['Nome']} possui a menor nota, {aluno_pior['Nota']}")

        
def relatoriogeral(alunos):
    file = "relatorio.txt"
    qtdaprovados(alunos)
    with open(file, "w") as file:
        file.write("Nome, Nota, Curso" + "\n")
        for aluno in alunos:
            file.write(f"{aluno['Nome']}, {aluno['Nota']}, {aluno['Curso']}\n")
        file.write(f"Media Geral: {mediageral(alunos)}\n")
        file.write(f"Total Aprovados: {aprovados}\n")
        file.write(f"Total Reprovados: {reprovados}\n")
        print("Relatório gerado com sucesso.")





def main():
    media = float(0)
    print("Programa Iniciado")
    alunos = carregar_alunos()
    print(f"O sistema possuí {len(alunos)} alunos cadastrados.")
    opcao = ""
    while opcao != "0":
        print(f" == SISTEMA DE CADASTRO ({len(alunos)} alunos)== ")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Buscar Aluno")
        print("4 - Remover Aluno")
        print("5 - Media Geral")
        print("6 - Verificar quantidade de alunos Aprovados e Reprovados")
        print("7 - Editar Nota")
        print("8 - Relatorio Geral")
        print("9 - Melhor e pior aluno.")
        print("0 - Sair")
        opcao = input("Informe opção que seja executar: ")

        if opcao == "1":
            alunos = cadastrar(alunos)
        elif opcao == "2":
            listar(alunos)
        elif opcao == "3":
            buscar(alunos)
        elif opcao == "4":
            alunos = remover(alunos)
        elif opcao == "5":
            media = mediageral(alunos)
            print(f"Media geral da turma: {media}")
        elif opcao == "6":
            qtdaprovados(alunos)
        elif opcao == "7":
            alunos = editarnota(alunos)
        elif opcao == "8":
            relatoriogeral(alunos)
        elif opcao == "9":
            comparamedia(alunos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção desconhecida, informe novamente.")
    salvar_alunos(alunos)

#Início do Programa

main()