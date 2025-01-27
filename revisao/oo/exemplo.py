# class Cachorro:
#     def __init__(self, nome, raca, cor, idade):
#         self.nome = nome
#         self.raca = raca
#         self.cor = cor
#         self.idade = idade
#         self.orelhas = 2
    
#     def latir(self):
#         print(f"{self.nome} diz: au au")

#     def corre(self, kms):
#         print(f"{self.nome} corre {kms} km")

# cachorro_da_diva = Cachorro("pitoco", "Vira-lata", "caramelo", 2)

# cachorro_da_diva.corre(35)

class Livro:
    def __init__(self, categoria, titulo, autor, indicacao):
        self.genero = categoria
        self.titulo = titulo
        self.autor = autor
        self.indicacao = indicacao

    def abrir(self, paginas):
        print(f"o livro {self.titulo} foi aberto na pagina {paginas}")

    def __str__(self):
        return f"{self.titulo} do genero {self.genero} escrita por {self.autor}"
    
    # classe que compara dois valores para verificar se é igual
    def __eq__(self, value): #value é COM O QUE ele está comparando
        if(isinstance(value, Livro)):
            titulo_igual = self.titulo == value.titulo
            autores_iguais = self.autor == value.autor
            return titulo_igual and autores_iguais
        else:
            return False
        

livro_da_kamila = Livro("romance", "crepusculo", "J.K. Rowling", 14)
livro_da_kamila.abrir(10)

print(livro_da_kamila)

        
    
        