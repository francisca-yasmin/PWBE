from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    idade = models.IntegerField()
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    escolaridade = models.CharField(max_length=255)
    bio = models.TextField()
    qtd_animais = models.PositiveIntegerField(null=True, blank=True)
    REQUIRED_FIELDS = ['telefone', 'idade']

    def __str__(self):
        return self.username


