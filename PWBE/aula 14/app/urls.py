from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), #as_view -> convertendo pra receber o request
    path('piloto/<int:pk>', view=PilotoRetrieveUpdateDestroyAPIView.as_view()),
]