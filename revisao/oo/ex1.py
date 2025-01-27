class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio
       
circulo = Circulo(5)
print(f"O calculo da área eh: {circulo.calcular_area()}")
print(f"O calculo do perimetro eh: {circulo.calcular_perimetro()}")
