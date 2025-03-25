from datetime import date, datetime, timedelta
# from django.shortcuts import render
from .models import Eventos
from .serializers import EventosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


#READ -> visualizar os eventos
@api_view(['GET']) #pegar as informações para mostrar para o usuário
def read_eventos(request):
    eventos = Eventos.objects.all()

    #filtrar por categoria/data e quantidade
    categoria = request.query_params.get('categoria')
    if categoria:
        eventos = eventos.filter(categoria__icontains = categoria)

    data = request.query_params.get('data')
    if data:
        eventos = eventos.filter(data__icontains = data)

    qtd_eventos = request.query_params.get('quantidade')
    if qtd_eventos:
        eventos = eventos[:int(qtd_eventos)]

    # filtra por odem de datas
    ordenar = request.query_params.get('ordenar')
    if ordenar:
        eventos = eventos.order_by('data').values()

    # filtrar por dias, pelos proximos 7 dias
    dias = request.query_params.get('dias')
    hoje = datetime.now()  # Data atual
    sete_dias = hoje + timedelta(days=7)
    if dias == "7-dias":
        eventos = eventos.filter(data__gte = hoje, data__lte = sete_dias)

    serializer = EventosSerializer(eventos, many=True) 
    return Response(serializer.data)


# get eventos -> filtrar por categoria, data e quantidade
@api_view(['GET'])
def pegar_evento(request, pk):
    try:
        evento = Eventos.objects.get(pk = pk)
    
    except Eventos.DoesNotExist:
        return Response({'erro': 'Evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(evento)
    return Response(serializer.data) #data -> dados


# post eventos -> usado para criar os eventos dentro do banco de dados
@api_view(['POST']) #-> cria eventos
def create_eventos(request):
    if request.method == 'POST':
        serializer = EventosSerializer(data=request.data, many=isinstance(request.data, list)) #converter para JSON
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#PUT -> atualiza os eventos de acordo com o desejo do usuário
@api_view(['PUT'])
def update_evento(request, pk):
    try:
        eventos = Eventos.objects.get(pk = pk)
    except Eventos.DoesNotExist:
        return Response({'erro': ' Evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(eventos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return  Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# função que deleta as informaçõs da chave fornecida pelo usuário
@api_view(['DELETE'])
def delete_evento(request, pk):
    try:
        eventos = Eventos.objects.get(pk = pk)
    except Eventos.DoesNotExist:
        return Response({'erro' : 'Evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    eventos.delete()
    return Response({'Mensagem': f'O seu evento foi apagado com sucesso'}, status=status.HTTP_200_OK)


