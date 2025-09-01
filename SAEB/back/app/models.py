from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    desc_tarefa = models.TextField()
    nome_setor = models.CharField(max_length=255)
    ESCOLHA_PRIORIDADES = (
        ('baixa',  'baixa'),
        ('media', 'media'),
        ('alta', 'alta')
    )
    prioridade = models.CharField(max_length=5, choices=ESCOLHA_PRIORIDADES, default='media')
    data_cadastro = models.DateField(auto_now_add=True),

    ESCOLHA_STATUS = (
        ('a fazer', 'a fazer'),
        ('fazendo', 'fazendo'),
        ('pronto', 'pronto')
    )

    status = models.CharField(max_length=10, choices=ESCOLHA_STATUS, default='a fazer')

    def __str__(self):
        return self.prioridade

