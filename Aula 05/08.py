import os

if os.path.exists("dados.txt"):
    print("Arquivo existe e será aberto.")
else:
    print("Arquivo inexistente.")