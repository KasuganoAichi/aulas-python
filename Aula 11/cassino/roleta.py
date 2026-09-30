import random

class Roleta:
    def __init__(self):
        pass

    def girar(self):
        return random.randint(0,36)

if __name__ == "__main__":
    print("Está em Roleta")