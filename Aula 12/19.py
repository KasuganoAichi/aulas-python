def validar_senha(senha):
	if len(senha) < 8:
		raise ValueError("A senha deve ter pelo menos 8 caracteres")

	if not any(caractere.isdigit() for caractere in senha):
		raise ValueError("A senha deve conter ao menos um número")


senha = input("Digite uma senha: ")

try:
	validar_senha(senha)
	print("Senha válida.")
except ValueError as erro:
	print(erro)
