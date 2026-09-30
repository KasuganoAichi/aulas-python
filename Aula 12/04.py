try:
    valor = int("python")
except ValueError as erro:
    print(f"Int não pode ser string. {erro}")