from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qtdRodas = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=255)
    escolhas_combustivel = (
        ('Gasolina', 'gasolina'),
        ('Etanol', 'etanol'),
        ('GNV', 'gnv'),
        ('Eletrico', 'eletrico'),
        ('Acool', 'alcool'),
        ('Diesel', 'dieses'),
        ('fb', 'feedback')
    )

    combustivel = models.CharField(max_length=9, choices=escolhas_combustivel)
    def __str__(self):
        return self.nome
    
