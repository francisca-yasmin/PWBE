from django.urls import path
from .views import PilotoListCreateAPIView

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()), #as_view -> convertendo pra receber o request
]