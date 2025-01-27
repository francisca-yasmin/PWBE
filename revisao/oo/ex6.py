class Produto:
    def __init__(self, nome, preco, valor_estoque):
        self.nome = nome
        self.preco = preco
        self.qtd = valor_estoque

    def calcular_estoque(self):
        return self.preco * self.qtd
    
    def verificar_produto(self):
        if self.qtd > 0:
            return " Disponivel"
        else:
            return "Indisponivel."
        
produto = Produto("Farinha", 26, 58)

print(f"O valor do estoque está avaliado em R${produto.calcular_estoque()} reais")
print(f"No momento a situação do produto eh: {produto.verificar_produto()}")