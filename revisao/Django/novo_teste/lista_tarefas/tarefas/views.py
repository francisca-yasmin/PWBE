
from django.shortcuts import render
from .models import Tarefas

def lista_postagens(request):
 tarefas = Tarefas.objects.all().order_by('-status')
 return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})
