from django.db import models

class Tarefas(models.Model):
 descricao = models.CharField(max_length=200)
 status = models.CharField(max_length=200)
 
 def __str__(self):
    return self.descricao
