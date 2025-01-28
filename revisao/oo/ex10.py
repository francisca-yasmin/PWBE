class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = True

    def verifica_disponivel(self):
        if self.disponivel:
            print("O livro esta disponivel para emprestimo")
        else:
            print("O livro não esta disponivel")

    def emprestar_livro(self):
        if self.disponivel:
            print("O livro foi emprestado.")
            self.disponivel = False
        else:
            print("O livro já foi emprestado, chegou tarde :( ")
    
    def devolver_livro(self):
        if not self.disponivel:
            print(f"O livro foi devolvido com sucesso")
            self.disponivel = True
    
livro = Livro("Amor & Gelato", "Jenna Evans", 320)

livro.verifica_disponivel()
print(f"O livro {livro.titulo} escrito por {livro.autor} contém {livro.paginas} paginas.")
