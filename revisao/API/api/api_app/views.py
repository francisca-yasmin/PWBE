from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def read_carros(request):
    carros = Carro.objects.all()
    serializer = CarroSerializer(carros, many=True) #nome da variavel que criamos
    return Response(serializer.data) #data -> dados


@api_view(['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk = pk)
    except Carro.DoesNotExist:
        return Response({'erro': ' Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializer(carro)
    return Response(serializer.data)


    