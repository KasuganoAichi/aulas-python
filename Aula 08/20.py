class Televisao:
    def __init__(self, marca, volume):
        self.marca = marca
        self._volume = 0
        self.volume = volume

        @property
        def volume(self):
            return self._volume

        @property
        def marca(self):
            return self._marca

        @volume.setter
        def volume(self, valor):
            if valor < 0:
                self._volume = 0
            elif valor > 100:
                self._volume = 100
            else:
                self._volume = valor

tv1 = Televisao("Samsung", 50)
print(f"Marca: {tv1.marca}")
print(f"Volume: {tv1.volume}")
tv1.volume = 120
print(f"Volume: {tv1.volume}")
tv1.volume = -30
print(f"Volume: {tv1.volume}")