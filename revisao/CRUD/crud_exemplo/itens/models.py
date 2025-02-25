from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    

    # classe que reescreve o nome 
    class Meta:
        verbose_name_plural = "Itens"
