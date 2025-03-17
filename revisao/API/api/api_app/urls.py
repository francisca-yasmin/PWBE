from django.urls import path
from . import views

urlpatterns = [
    path('carros/', views.read_carros),
    path('carros/buscar/<int:pk>', views.pegar_carro),
]