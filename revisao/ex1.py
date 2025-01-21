# n1 = int(input("Digite um numero: "))
# n2 = int(input("Digite um numero: "))

# soma = n1 + n2
# print("A soma dos dois numeros fornecidos eh: ", soma)

########################################

#exercicio 2 - condicionais 

# n1 = int(input("Digite um numero: "))

# if n1 % 2 == 0:
#     print("o numero digitado eh par")
# else:
#     print("O numero digitado eh impar")

#########################################

#exercicio 3 - laços de repetição

# num = int(input("digite um numero: "))

# for i in range(0, num + 1):
#     print(i)

#########################################

#exercicio 4 - função

s = input("digite uma palavra: ")

def inverter_strings(s):

    inverso = ""

    for i in s:
        inverso = i + inverso
    return inverso
    
print(inverter_strings(s))