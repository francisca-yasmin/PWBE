from django.urls import path
from . import views

urlpatterns = [
    path('evento/', views.read_eventos),
    path('evento/buscar/<int:pk>', views.pegar_evento),
    path('evento/criar/', views.create_eventos),
    path('evento/atualizar/<int:pk>', views.update_evento),
    path('evento/deletar/<int:pk>', views.delete_evento)
]

