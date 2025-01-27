class Funcionario:
    def __init__(self, nome, salario, cargo, beneficios, impostos):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo 
        self.beneficios = beneficios
        self.imposto = impostos

    def calcula_salario_liquido(self):
        desconto_imposto = (self.imposto / 100) * self.salario
        salario_liquido = self.salario - desconto_imposto + self.beneficios
        return salario_liquido
    
    
funcionario = Funcionario("fran", 8000, "Desenvolvedora de Software", 800, 10)

print(f"O funcionário {funcionario.nome} possui o cargo {funcionario.cargo}")
print(f"O seu salario atual eh de {funcionario.salario} e tem os beneficios no valor de {funcionario.beneficios}")
print(f"O imposto que foi descontado do salario foi no valor de {funcionario.imposto}%")

   
        