from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView #retrive ->
from .serializers import PilotoSerializer
from .models import Piloto
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

# PILOTO
class PilotoPaginacao(PageNumberPagination):
    page_size = 5 #tamanho (inicial) da pagina
    page_query_param = 'page_size'
    max_page_size = 10 

class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk' # canmpo que eu vou consultar pra fazer as coisas que eu preciso


class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    def get_queryset(self):
        queryset = super().get_queryset() #super -> chamando a classe pai
        #verifica se o nome foi preenchido
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        #se a equipe não for da ds16 e tentar colocar nos 5 primeiros, é lançado um erro
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 deve ficar entre os 5 primeiros')
        serializer.save()
    
    

