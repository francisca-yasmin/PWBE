# ano_nasc = int(input("digite o ano do seu nascimento: "))
# nome = input("digite o seu nome: ")

# idade = 2025 - ano_nasc
# print("a sua idade em 2025 vai ser de: ", idade)

##########################################

#exercicio 2 - condicionais

# nota1 = float(input("digite uma nota: "))
# nota2 = float(input("digite uma nota: "))
# nota3 = float(input("digite uma nota: "))
# nota4 = float(input("digite uma nota: "))
# nota5 = float(input("digite uma nota: "))

# media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
# if media >= 5:
#     print("parabens, você fez a sua obrigação e foi APROVADO!")

# elif media > 2.5 and media < 5:
#     print("que pena, REPROVADO :(")

# else:
#     print("REPROVADO :(")

#####################################

#exercicio 3 - laços de repetição

# numero_maior = 0

# while True:
#     num = int(input("digite um numero: "))

#     if num < 0:
#         break

#     if numero_maior < num:
#         numero_maior = num

#     if num == numero_maior:
#         print("o maior numero fornecido foi: ", numero_maior)   

######################################

# eercicio 4 - função

s = input("digite uma palavra qualquer: ")

def contar_caracteres(s):

    dicionario = {}
    for i in s:
        if i in dicionario:
            dicionario[i] += 1
        else:
           dicionario[i] = 1
    return dicionario

print(contar_caracteres(s))


