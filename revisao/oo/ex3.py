class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo = Retangulo(8, 5)

print(f"Area do Retangulo: {retangulo.calcular_area()}")
print(f"O perimetro do Retangulo eh: {retangulo.calcular_perimetro()}")