class Circle:
    def __init__(self, center, raio):
        self.center = center
        self.raio = raio

    @property
    def area(self):
        return 3,14*self.raio**2
    
    def grafico(self):
        pass
