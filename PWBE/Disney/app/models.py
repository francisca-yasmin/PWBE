from django.db import models
from django.contrib.auth.models import AbstractUser #criar ussuario personalizado

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)



class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    genero_escolhas=( 
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('N', 'Prefiro não informar')

    )
    genero = models.CharField(max_length=100, choices=genero_escolhas, null=True, blank=True)
    escolha_colaborador = (
        ('G', 'Gestor'),
        ('E', 'Estagiario'),
        ('A', 'Aprendiz'),
        ('M', 'Meio Oficial')

    )
    colaborador = models.CharField(max_length=1, choices=escolha_colaborador, default='A')
    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
