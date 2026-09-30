def multiplicar_elementos(lista, fator):
	for elemento in lista:
		try:
			resultado = elemento * fator
			print(f"Resultado: {resultado}")
		except TypeError as erro:
			print(f"Erro: {erro}")
		finally:
			print("Item processado")


lista_mista = [10, "Python", 4.5, None]
multiplicar_elementos(lista_mista, 2)
