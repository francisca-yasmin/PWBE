from django.urls import path
from . import views

urlpatterns = [
    path('evento/', views.read_eventos),
    path('evento/buscar/<int:pk>', views.pegar_evento),
    path('evento/criar/', views.create_eventos)
]

