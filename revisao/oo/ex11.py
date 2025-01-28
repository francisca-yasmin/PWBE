class Banco:
    def __init__(self, dinheiro):
        self.dinheiro = dinheiro
        self.clientes = []

    def cadastar_cliente(self):
       nome = input("Digite o seu nome: ")
       self.clientes.append(nome)

       cpf = input("Digite seu CPF (apenas numeros): ")
       telefone = input("Digite seu telefone (apenas numeros): ")

       return "Seu cadastro foi feito com sucesso."
       
    def deposito(self):
        deposito = float(input("Digite o valor que gostaria de depositar: "))
        self.dinheiro += deposito
        return f"O deposito de R${deposito} reais foi realizado com sucesso."
    
    def saque(self):
        saque = float(input("Digite o valor que gostaria de sacar: "))
        self.dinheiro -= saque
        return f"O saque de R${saque} reais foi um sucesso."
    
    def tranferir_dinheiro(self):
        valor = float(input("Qual o valor que você gostaria de tranferir? "))
        while True:
            quem = input("Digite o numero da conta para quem você vai transferir: ")

            if not quem.isdigit():
                print("Digite apenas valores numericos: ")
            break

        return f"A tranferencia para {quem} no valor de R${valor} reais, foi um sucesso."
    
    def menu(self):
        print("Bem vindo ao Banco do Brasil. Vamos realizar seu cadastro.")
        self.cadastar_cliente()
        while True:
            print("[1] Saque"
                "\n[2] Deposito"
                "\n[3] Transferência")
            opcao = int(input("\nEscolha ao que deseja fazer: "))
            if opcao == 1:
                self.saque()
            elif opcao == 2:
                self.deposito()
            elif opcao == 3:
                self.tranferir_dinheiro()
            else:
                break
banco = Banco(5000)
banco.menu()
