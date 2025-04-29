from django.urls import path
from .views import *

urlpatterns = [
    path('usuario/', UsuarioListCreateAPIView.as_view()),
    path('ingresso/', IngressoRetriveUpdateDestroyAPIView.as_view())
    path('ingresso/<int:pk>', IngressoRetriveUpdateDestroyAPIView.as_view()),
    path('login/', LoginView.as_view())
]