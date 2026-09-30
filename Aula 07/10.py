class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada

    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print("A lâmpada foi ligada.")
        else:
            print("A lâmpada já está ligada.")

    def desligar(self):
        if self.ligada:
            self.ligada = False
            print("A lâmpada foi desligada.")
        else:
            print("A lâmpada já está desligada.")

    def estado(self):
        if self.ligada:
            print("A lâmpada está ligada.")
        else:
            print("A lâmpada está desligada.")


lampada = Lampada()
lampada.estado()
lampada.ligar()
lampada.estado()
lampada.desligar()
lampada.estado()