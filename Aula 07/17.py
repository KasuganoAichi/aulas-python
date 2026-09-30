class Termometro:
    def __init__(self, temperatura_celsius):
        self.temperatura_celsius = temperatura_celsius

    def obter_fahrenheit(self):
        return (self.temperatura_celsius * 1.8) + 32

temperatura = Termometro(25)
print(f"Temperatura em Celsius: {temperatura.temperatura_celsius}°C")
temperatura_fahrenheit = temperatura.obter_fahrenheit()
print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit}°F")