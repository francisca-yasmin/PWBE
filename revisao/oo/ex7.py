class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def verifica_triangulo(self):
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if not self.verifica_triangulo():
            raise ValueError("O triângulo não é válido")
        
        semi_perimetro = (self.lado1 + self.lado2 + self.lado3)/2
        area = (semi_perimetro * (semi_perimetro - self.lado1) * 
                    (semi_perimetro - self.lado2) * (semi_perimetro - self.lado3)) ** 0.5
        return area

triangulo = Triangulo(3,4,5)
if triangulo.verifica_triangulo():
    print("o triangulo é valido")
    print("area do triangulo: ", triangulo.calcular_area())
else:
    print("O triangulo não é válido")
