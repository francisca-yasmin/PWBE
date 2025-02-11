# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio

#     def calcular_area(self):
#         return 3.14 * self.raio ** 2

#     def calcular_perimetro(self):
#         return 2 * 3.14 * self.raio
       
# circulo = Circulo(5)
# print(f"O calculo da área eh: {circulo.calcular_area()}")
# print(f"O calculo do perimetro eh: {circulo.calcular_perimetro()}")

########################################################################

# EXERCICIO 02
# class ContaBancaria:
#     def __init__(self, conta, nome):
#         self.numero_conta = conta
#         self.titular_conta = nome
#         self.saldo_conta = 0
        
    
#     def depositar(self, deposito):
#         if deposito < 0:
#             return "Não é possivel depositar valores negativos"
#         else:
#             self.saldo_conta += deposito
#             return "Deposito bem sucedido"

#     def sacar(self, saque):
#         if saque > self.saldo_conta:
#             return "Não é possivel realizar esse saque"
#         else:
#             self.saldo_conta -= saque
#             return "Saque bem sucedido"
        
#     def __str__(self):
#         return f"O saldo da conta de {self.titular_conta} eh {self.saldo_conta}"


# banco = ContaBancaria(0000, "Fran")
# banco.depositar(1500)
# banco.sacar(500)

# print(banco)    

################################################################################

# EXERCICIO 3
# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
    
#     def calcular_area(self):
#         return self.largura * self.altura
    
#     def calcular_perimetro(self):
#         return 2 * (self.largura + self.altura)
    
# retangulo = Retangulo(8, 5)

# print(f"Area do Retangulo: {retangulo.calcular_area()}")
# print(f"O perimetro do Retangulo eh: {retangulo.calcular_perimetro()}")

##########################################################################

# EXERCICIO 4

# class Aluno:
#     def __init__(self, nome, nota1, nota2, ):
#         self.nome = nome
#         self.nota1 = nota1
#         self.nota2 = nota2

#     def calcular_media(self):
#         return (self.nota1 + self.nota2) // 2
    
#     def verificar_situacao(self):
#         if self.calcular_media() < 6:
#             return "Reprovado"
#         else:
#             return "Aprovado"

# aluno = Aluno("Fran", 9, 8)
# print(f"A media das notas do aluno {aluno.nome} eh de {aluno.calcular_media()}")
# print(f"A situação atual do(a) aluno(a) {aluno.nome} eh {aluno.verificar_situacao()}")

##########################################################################

# EXERCICIO 5

# class Funcionario:
#     def __init__(self, nome, salario, cargo, beneficios, impostos):
#         self.nome = nome
#         self.salario = salario
#         self.cargo = cargo 
#         self.beneficios = beneficios
#         self.imposto = impostos

#     def calcula_salario_liquido(self):
#         desconto_imposto = (self.imposto / 100) * self.salario
#         salario_liquido = self.salario - desconto_imposto + self.beneficios
#         return salario_liquido
    
    
# funcionario = Funcionario("fran", 8000, "Desenvolvedora de Software", 800, 10)

# print(f"O funcionário {funcionario.nome} possui o cargo {funcionario.cargo}")
# print(f"O seu salario atual eh de {funcionario.salario} e tem os beneficios no valor de {funcionario.beneficios}")
# print(f"O imposto que foi descontado do salario foi no valor de {funcionario.imposto}%")
    
##########################################################################

# EXERCICIO 6 
# class Produto:
#     def __init__(self, nome, preco, valor_estoque):
#         self.nome = nome
#         self.preco = preco
#         self.qtd = valor_estoque

#     def calcular_estoque(self):
#         return self.preco * self.qtd
    
#     def verificar_produto(self):
#         if self.qtd > 0:
#             return " Disponivel"
#         else:
#             return "Indisponivel."
        
# produto = Produto("Farinha", 26, 58)

# print(f"O valor do estoque está avaliado em R${produto.calcular_estoque()} reais")
# print(f"No momento a situação do produto eh: {produto.verificar_produto()}")

##########################################################################

# EXERCICIO 7

# class Triangulo:
#     def __init__(self, lado1, lado2, lado3):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.lado3 = lado3

#     def verifica_triangulo(self):
#         return (self.lado1 + self.lado2 > self.lado3 and
#                 self.lado1 + self.lado3 > self.lado2 and
#                 self.lado2 + self.lado3 > self.lado1)

#     def calcular_area(self):
#         if not self.verifica_triangulo():
#             raise ValueError("O triângulo não é válido")
        
#         semi_perimetro = (self.lado1 + self.lado2 + self.lado3)/2
#         area = (semi_perimetro * (semi_perimetro - self.lado1) * 
#                     (semi_perimetro - self.lado2) * (semi_perimetro - self.lado3)) ** 0.5
#         return area

# triangulo = Triangulo(3,4,5)
# if triangulo.verifica_triangulo():
#     print("o triangulo é valido")
#     print("area do triangulo: ", triangulo.calcular_area())
# else:
#     print("O triangulo não é válido")

##########################################################################

# EXERCICIO 8

# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = 0

#     def acelerar(self, incremento):
#         if incremento > 0:
#             self.velocidade += incremento
#             print(f"Você está acelerando, sua velocidade agora eh {self.velocidade} km/h")
        
#     def frear(self, decremento):
#         if decremento > 0:
#             self.velocidade -= decremento

#         if self.velocidade < 0:
#             self.velocidade = 0
#             print(f"Você apertou o freio. sua velocidade atual agora eh {self.velocidade} km/h")

#     def mostrar_velocidade(self):
#         print(f"O carro da marca {self.marca}, do modelo {self.modelo}, está com a velocidade de {self.velocidade}")


# carro = Carro("Toyota", "Corolla")

# carro.acelerar(100)
# carro.acelerar(50)
# carro.frear(30)
# carro.mostrar_velocidade()

##########################################################################

# EXERCICIO 9

# class Paciente:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         self.historico = ['papa nicolau', 'exame de sangue']

#     def adicionar_consulta(self):
#         nova_consulta = input("Adicionar consulta ao historico: ")
#         self.historico.append(nova_consulta)
#         print(f"A consulta {nova_consulta} foi adicionada a lista de consultas.")

#     def exibir_historico(self):
#         print("\n###### HISTORICO DE CONSULTAS ######")
#         print(self.historico)

# paciente = Paciente("Fran", 19)

# paciente.adicionar_consulta()
# paciente.exibir_historico()


##########################################################################

# EXERCICIO 10

# class Livro:
#     def __init__(self, titulo, autor, paginas):
#         self.titulo = titulo
#         self.autor = autor
#         self.paginas = paginas
#         self.disponivel = True

#     def verifica_disponivel(self):
#         if self.disponivel:
#             print("O livro esta disponivel para emprestimo")
#         else:
#             print("O livro não esta disponivel")

#     def emprestar_livro(self):
#         if self.disponivel:
#             print("O livro foi emprestado.")
#             self.disponivel = False
#         else:
#             print("O livro já foi emprestado, chegou tarde :( ")
    
#     def devolver_livro(self):
#         if not self.disponivel:
#             print(f"O livro foi devolvido com sucesso")
#             self.disponivel = True
    
# livro = Livro("Amor & Gelato", "Jenna Evans", 320)

# livro.verifica_disponivel()
# print(f"O livro {livro.titulo} escrito por {livro.autor} contém {livro.paginas} paginas.")

##########################################################################

# EXERCICIO 11

# class Banco:
#     def __init__(self, dinheiro):
#         self.dinheiro = dinheiro
#         self.clientes = []

#     def cadastar_cliente(self, nome):
#        nome = input("Digite o seu nome: ")
#        self.clientes.append(nome)

#        cpf = input("Digite seu CPF (apenas numeros): ")
#        telefone = input("Digite seu telefone (apenas numeros): ")

#        return "Seu cadastro foi feito com sucesso."
       
#     def deposito(self):
#         deposito = float(input("Digite o valor que gostaria de depositar: "))
#         self.dinheiro += deposito
#         return f"O deposito de R${deposito} reais foi realizado com sucesso."
    
#     def saque(self):
#         saque = float(input("Digite o valor que gostaria de sacar: "))
#         self.dinheiro -= saque
#         return f"O saque de R${saque} reais foi um sucesso."
    
#     def tranferir_dinheiro(self):
#         valor = float(input("Qual o valor que você gostaria de tranferir? "))
#         while True:
#             quem = input("Digite o numero da conta para quem você vai transferir: ")

#             if not quem.isdigit(): #converter o input do usuário em numeros
#                 print("Digite apenas valores numericos: ")
#             break

#         return f"A tranferencia para {quem} no valor de R${valor} reais, foi um sucesso."
    
#     def menu(self):
#         print("Bem vindo ao Banco do Brasil. Vamos realizar seu cadastro.")
#         self.cadastar_cliente()
#         while True:
#             print("[1] Saque"
#                 "\n[2] Deposito"
#                 "\n[3] Transferência")
#             opcao = int(input("\nEscolha ao que deseja fazer: "))
#             if opcao == 1:
#                 self.saque()
#             elif opcao == 2:
#                 self.deposito()
#             elif opcao == 3:
#                 self.tranferir_dinheiro()
#             else:
#                 break
# banco = Banco(5000)
# banco.menu()

##########################################################################

# EXERCICIO 12

# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco


# class LojaVirtual:
#     def __init__(self):
#         self.produtos = []
#         self.carrinho = []
#         # self.produto = Produto()

#     def cadastrar_produtos(self, nome, preco):
#         self.produto = Produto(nome, preco)
#         self.produtos.append(produto)
#         print(f"O produto {nome} foi adicionado com sucesso!")

#     def gerar_carrinho(self):
#         if self.produto in self.produtos:
#             self.carrinho.append(self.produto)
#             print("O produto foi adicionado ao carrinho.")
#         else:
#             print("O produto não foi encontrado.")
    
#     def aplicar_desconto(self, porcentagem):
#         if self.produto in self.carrinho:
#             self.produto.preco -= self.produto.preco * (porcentagem / 100)
#             print("o desconto foi aplicado")
#         else:
#             print("Sua compra não é possivel aplicar desconto.")
            
#     def valor_total(self, total):
#         total = sum(self.preco for self.produto in self.carrinho)
#         print(f"A sua compra ficou num total de R${total} reais")

# produto = Produto("pulseira", "20")

# loja = LojaVirtual()

# #cadastro de produtos
# loja.cadastrar_produtos("Relogio Cassio", 200)
# loja.cadastrar_produtos("Camiseta Overside", 300)

# #gerar carrinho
# loja.gerar_carrinho()


# #aplicar o desconto
# loja.aplicar_desconto(15)

##########################################################################

# EXERCICIO 13

# class Contato:
#     def __init__(self, nome, numero_telefone):
#         self.nome = nome 
#         self.telefone = numero_telefone


# class Agenda:
#     def __init__(self):
#         self.lista_contatos = []

#     def cadastrar_numeros(self, nome, numero_telefone):
#         contato_novo = Contato(nome,numero_telefone)
#         self.lista_contatos.append(contato_novo)
#         print(f"O contato {nome} foi adicionado na Agenda.")

#     def editar_lista(self, nome, novo_nome = None):
#         if nome in self.lista_contatos:
#             novo_nome = print("digite o novo nome na lista de contatos: ")
#             self.lista_contatos.append(novo_nome)
#             print(f"{nome} foi mudado para {novo_nome}")
            
#         else:
#             print("o nome não existe na agenda.")

#     def remover_contato(self, nome):
#         if nome in self.lista_contatos:
#             nome_removido = print(f"digite o nome que deseja remover da agenda: ")
#             self.lista_contatos.remove(nome_removido)
#             print(f"{nome_removido} removido da agenda")

#     def busca_contato(self, nome):
#         contato_encontrado = [contato.nome for contato in self.lista_contatos if nome.lower() in contato.nome.lower()]
#         if contato_encontrado:
#             print(f"o contato {contato_encontrado} esta presente na lista.")
#         else:
#             print("o contato não está presente na lista")


# agenda = Agenda()

# agenda.cadastrar_numeros("Fran", "123456789")
# agenda.cadastrar_numeros("adrian", "987654321")

# agenda.editar_lista("", novo_nome = "bruno")

# agenda.remover_contato("Fran")

# agenda.busca_contato("adrian")
    
##########################################################################

# EXERCICIO 14

# class Produto:
#     def __init__(self, nome, preco, qtd_produto):
#         self.nome = nome
#         self.preco = preco
#         self.qtd = qtd_produto

# class MaquinaDeVendar:
#     def __init__(self):
#         self.produtos = {}
#         self.dinheiro = 0

#     def cadastrar_produtos(self, nome, preco, qtd_produto):
#         if nome in self.produtos:
#             nome = input("Digite o produto que deseja cadastrar: ")
#             self.produto[nome].qtd_produto += qtd_produto
#         else:
#             self.produtos[nome] = Produto(nome, preco, qtd_produto)
#             print ("Produto cadastrado com sucesso")

#     def selecionar_produto(self, nome_produto):
#         if nome_produto in self.produtos:
#             produto = self.produtos[nome_produto] #consulta o dicionario produtos
#             if self.produto.qtd_produto > 0:
#                 return produto
#             else:
#                 print(f"O produto {nome_produto} está esgotado")

#     def inserir_dinheiro(self, valor):
#         if valor > 0:
#             self.dinheiro += valor
#             print(f"Seu saldo atual agora eh: R${self.dinheiro:.2f}")
#         else:
#             print("não tem troco a ser devolvido.")

#     def retornar_troco(self, preco_produto):
#         if self.dinheiro > preco_produto:
#             troco = self.dinheiro - preco_produto
#             self.dinheiro = 0
#             print(f"O seu troco eh de: R${troco}")

#     def exibir_estoque(self):
#         print("\nEstoque disponivel: ")
#         for produto in self.produtos:
#             print(produto)


# maquina = MaquinaDeVendar()

# #cadastrando produtos na maquina
# maquina.cadastrar_produtos("kit-kat", 10.0, 25)
# maquina.cadastrar_produtos("Chocolate Meio amargo", 20.0, 30)

# maquina.exibir_estoque()

# maquina.inserir_dinheiro(50.0)

# maquina.exibir_estoque()

##########################################################################

# EXERCICIO 15

##########################################################################

# EXERCICIO 16

##########################################################################

# EXERCICIO 17

# class Livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor
#         self.disponivel = True

#     def __str__(self):
#         return f"{self.titulo} de {self.autor}"

# class Biblioteca:
#     def __init__(self):
#         self.livros = []
    
#     def cadastrar_livros(self):
#         titulo = input("Digite o titulo do livro que deseja cadastrar:  ")
#         autor = input("Digite o autor do livro: ")

#         novo_livro = Livro(titulo, autor)
#         self.livros.append(novo_livro)
#         print(f"{novo_livro} cadastrado com sucesso")

#     def emprestar_livro(self, titulo):
#         for titulo in self.livros:
#                 if titulo.disponivel:
#                     print("O livro foi emprestado.")
#                     titulo.disponivel = False
#                     return
#                 else:
#                     print("O livro já foi emprestado, chegou tarde :( ")

#     def verifica_disponivel(self, titulo):
#         if titulo in self.livros:
#              print("O livro esta disponivel para emprestimo")
#         else:
#             print("O livro não esta disponivel")


# biblioteca = Biblioteca()
# biblioteca.cadastrar_livros()

# titulo = input("\nDigite o titulo do livro para verificar disponibilidade: ")
# biblioteca.verifica_disponivel(titulo)

# biblioteca.emprestar_livro(titulo) #empresta o livro caso esteja dispnivel

##########################################################################

# EXERCICIO 18
# import calendar
# from datetime import datetime

# class Calendario:
#     def __init__(self):
#         self.feriados = {
#             "01-01", #ano novo
#             "25-12", # natal
#             "07-09" # independencia do Brasil 
#         }

#     def exibir_calendario(self):
#         pass

#     def verifica_feriado(self):
#         pass

#     def Difere_datas(self):
#         pass

##########################################################################

# EXERCICIO 19

# import random

# class JogoAdivinhacao:
#     def __init__(self, min = 1, max = 100):
#         self.num_secreto = random.randint(min, max)
#         self.min = min
#         self.max = max
#         self.tentativas = 0

#     def palpite(self):
#         while True:
#             self.tentativas += 1
#             try:
#                 palpite = int(input(f"\nDigite o palpite entre {self.min} e {self.max}: "))
#                 if palpite < self.num_secreto:
#                     print("O numero eh maior. Tente de novo ")
#                 elif palpite > self.num_secreto:
#                     print("O numero eh menor. Tente novamente")
#                 elif palpite == self.num_secreto:
#                     print("Voce acertou o numero! Parabens")
#                     break
#                 else:
#                     print(f"Infelizmente você errou. O numero era {self.num_secreto}.")
#             except ValueError:
#                 print("Digite um valor valido.")

# jogo = JogoAdivinhacao()

# jogo.palpite()

##########################################################################

# EXERCICIO 20
