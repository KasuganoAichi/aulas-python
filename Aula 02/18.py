file = input("Informe o nome do arquivo: ").strip().lower()

if file.endswith(".pdf") or file.endswith(".doc"):
    print("Arquivo válido.")
else:
    print("Arquivo inválido.")