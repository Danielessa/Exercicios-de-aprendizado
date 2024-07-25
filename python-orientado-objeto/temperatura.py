class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    def farenheit(self):
        return self._celsius * 9/5 + 32

temp  = int(input('Temperatura(°C): '))
termometro = Temperatura(temp)
print(f'Temperatura em feirenheit {termometro.farenheit()} e em graus celsius {termometro.celsius}')
