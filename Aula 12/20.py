nome_arquivo = input("Digite o nome do arquivo .txt: ")

try:
	with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
		conteudo = arquivo.read()
		print(conteudo)
except FileNotFoundError:
	print("Arquivo não encontrado. Verifique o nome digitado.")
except Exception as erro:
	print(f"Ocorreu um erro inesperado: {erro}")
finally:
	print("Encerrando rotina de leitura de arquivos.")
