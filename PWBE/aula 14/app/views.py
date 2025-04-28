from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView #retrive ->
from .serializers import PilotoSerializer, CarroSerializer
from .models import Piloto, Carro
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# PILOTO
class PilotoPaginacao(PageNumberPagination):
    page_size = 5 #tamanho (inicial) da pagina
    page_query_param = 'page_size'
    max_page_size = 10 

# classe para pegar e ciar um piloto
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


    # documentacao da classe piloto
    @swagger_auto_schema( #listar todos os pilotos
            operation_description='Lista todos os pilotos de Formula 1',
            responses={ 
                200: PilotoSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING

                )
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    #criar o piloto
    @swagger_auto_schema(
            operation_description='Cria um novo piloto',
            request_body=PilotoSerializer,
            responses={
                201: PilotoSerializer,
                400: 'error'
            }
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

   
# consultar, atualizar e deletar um piloto
class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk' # campo que eu vou consultar pra fazer as coisas que eu preciso

    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    #DELETE do piloto
    @swagger_auto_schema(
            operation_description='Deletar um piloto pelo sesu Id',
            responses={
                204: 'No Content',
                404: 'Not Found'
            }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    #ATUALIZAR um piloto pelo id
    @swagger_auto_schema(
        operation_description= 'Atualizar um piloto pelo id',
        request_body=PilotoSerializer,
        responses={
            200: PilotoSerializer,
            400: 'Error'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    

##################################################CARRO

class CarroPaginacao(PageNumberPagination):
    page_size = 5 
    page_query_param = 'page_size'
    max_page_size = 10
    

#criar e listar os dados de carros
class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    def get_queryset(self):
        queryset = super().get_queryset() #super -> chamando a classe pai
        #verifica se o nome foi preenchido
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset


    # documentacao da classe carro
    @swagger_auto_schema( #listar todos os carror
            operation_description='Lista todos os Carros de Formula 1',
            responses={ 
                200: CarroSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do carro',
                    type=openapi.TYPE_STRING

                )
            ]
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    #criar o carro
    @swagger_auto_schema(
            operation_description='Cria um novo carro',
            request_body=CarroSerializer,
            responses={
                201: CarroSerializer,
                400: 'error'
            }
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    




