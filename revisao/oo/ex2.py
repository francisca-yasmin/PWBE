class ContaBancaria:
    def __init__(self, conta, nome):
        self.numero_conta = conta
        self.titular_conta = nome
        self.saldo_conta = 0
        
    
    def depositar(self, deposito):
        if deposito < 0:
            return "Não é possivel depositar valores negativos"
        else:
            self.saldo_conta += deposito
            return "Deposito bem sucedido"

    def sacar(self, saque):
        if saque > self.saldo_conta:
            return "Não é possivel realizar esse saque"
        else:
            self.saldo_conta -= saque
            return "Saque bem sucedido"
        
    def __str__(self):
        return f"O saldo da conta de {self.titular_conta} eh {self.saldo_conta}"


banco = ContaBancaria(0000, "Fran")
banco.depositar(1500)
banco.sacar(500)

print(banco)    