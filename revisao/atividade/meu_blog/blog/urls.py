from django.urls import path
from . import views

urlpatterns = [
 path('', views.listar_acervo, name='listar_acervo'),
 path('cadastrar/', views.cadastrar_livro, name='cadastro_livro'),
 path('atualizar/<int:pk>/', views.atualizar_livro, name='atualizar'),
 path('deletar/<int:pk>/', views.remove_livro, name='deletar'),
]