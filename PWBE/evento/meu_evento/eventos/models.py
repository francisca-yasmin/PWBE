from django.db import models

class Eventos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    local = models.CharField(max_length=255)
    data = models.DateTimeField()
    categoria_escolha = (
        ('musica', 'Musica'),
        ('palestra', 'Palestra'),
        ('workshop', 'Workshop'),
        ('filmes', 'Filmes'),
    )

    categoria = models.CharField(max_length=10, choices=categoria_escolha)

    def __str__(self):
        return self.nome

