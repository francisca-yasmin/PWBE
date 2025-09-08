from django.urls import path
from .views import *

urlpatterns = [
    path('usuario/', UsuarioListCreate.as_view()),
    path('tarefa/', TarefaListCreate.as_view()),
    path('tarefa/<int:pk>/', TarefaRetriveUpdateDestroy.as_view())
]
