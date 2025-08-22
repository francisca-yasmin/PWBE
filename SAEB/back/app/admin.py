from django.contrib import admin
from .models import Usuario, Tarefa

#registrar minhas tabelas no banco de dados
admin.site.register(Usuario)
admin.site.register(Tarefa)
