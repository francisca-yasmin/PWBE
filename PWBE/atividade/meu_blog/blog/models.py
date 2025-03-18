from django.db import models


class Biblioteca(models.Model):
    nome_livro = models.CharField(max_length=200)
    autor_livro = models.TextField()
    data_publicacao = models.DateTimeField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome_livro
