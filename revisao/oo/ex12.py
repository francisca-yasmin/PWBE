class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class LojaVirtual:
    def __init__(self):
        self.produtos = []
        self.carrinho = []
        # self.produto = Produto()

    def cadastrar_produtos(self, nome, preco):
        self.produto = Produto(nome, produto)
        self.produtos.append(produto)
        print(f"O produto {nome} foi adicionado com sucesso!")

    def gerar_carrinho(self):
        if self.produto in self.produtos:
            self.carrinho.append(self.produto)
            print("O produto foi adicionado ao carrinho.")
        else:
            print("O produto não foi encontrado.")
    
    def aplicar_desconto(self, porcentagem):
        if self.produto in self.carrinho:
            self.produto.preco -= self.produto.preco * (porcentagem / 100)
            print("o desconto foi aplicado")
        else:
            print("Sua compra não é possivel aplicar desconto.")
            
    def valor_total(self, total):
        total = sum(self.preco for self.produto in self.carrinho)
        print(f"A sua compra ficou num total de R${total} reais")

produto = Produto("arroz", 12)

loja = LojaVirtual()

#cadastro de produtos
loja.cadastrar_produtos("Relogio Cassio", 200)
loja.cadastrar_produtos("Camiseta Overside", 300)

#gerar carrinho
loja.gerar_carrinho()


#aplicar o desconto
loja.aplicar_desconto(15)


        
            