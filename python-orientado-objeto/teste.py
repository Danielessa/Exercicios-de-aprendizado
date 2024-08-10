class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Teste
temp = Temperatura(25)
print(f'Temperatura em Celsius: {temp.celsius}°C')
print(f'Temperatura em Fahrenheit: {temp.fahrenheit}°F')