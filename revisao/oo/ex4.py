class Aluno:
    def __init__(self, nome, nota1, nota2, ):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) // 2
    
    def verificar_situacao(self):
        if self.calcular_media() < 6:
            return "Reprovado"
        else:
            return "Aprovado"

aluno = Aluno("Fran", 9, 8)
print(f"A media das notas do aluno {aluno.nome} eh de {aluno.calcular_media()}")
print(f"A situação atual do(a) aluno(a) {aluno.nome} eh {aluno.verificar_situacao()}")