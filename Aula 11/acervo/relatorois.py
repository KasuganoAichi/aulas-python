def mais_antigo(livros):
    ano = 2026
    for livro in livros:
        if livro.ano < ano:
            ano = livro.ano
            antigo = livro
    return antigo

def recentes(livros):
    recentes = []
    for livro in livros:
        if livro.eh_recente():
            recentes.append(livro)
    return recentes