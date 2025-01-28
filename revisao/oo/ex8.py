class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, incremento):
        if incremento > 0:
            self.velocidade += incremento
            print(f"Você está acelerando, sua velocidade agora eh {self.velocidade} km/h")
        
    def frear(self, decremento):
        if decremento > 0:
            self.velocidade -= decremento

        if self.velocidade < 0:
            self.velocidade = 0
            print(f"Você apertou o freio. sua velocidade atual agora eh {self.velocidade} km/h")

    def mostrar_velocidade(self):
        print(f"O carro da marca {self.marca}, do modelo {self.modelo}, está com a velocidade de {self.velocidade}")


carro = Carro("Toyota", "Corolla")

carro.acelerar(100)
carro.acelerar(50)
carro.frear(30)
carro.mostrar_velocidade()


