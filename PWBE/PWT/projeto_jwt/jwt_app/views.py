from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def criar_user(request):
    
    username = request.data.get('username')
    senha = request.data.get('senha')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    bio = request.data.get('bio')
    qtd_animais = request.data.get('qtd_animais')
    #verifica se os campos obrigatorios estão completos
    if not username or not idade or not telefone:
        return Response({'erro': 'campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(telefone=telefone).exists():
        return Response({'erro': f'Esse telefone {telefone} já existe em outro cadastro'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuario.objects.create_user(
        username = username,
        password = senha,
        idade = idade,
        telefone = telefone,
        endereco = endereco,
        escolaridade = escolaridade,
        bio = bio,
        qtd_animais = qtd_animais
    )
    return Response({'Mensagem': f'usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)    

@api_view(['POST'])
def logar_user(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    #verifica se o usuario realmente existe
    #se existir retorna os dados, mas se não, não mostra nada
    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)

        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'erro': 'usuario e/ou senha incorretos'}, status=status.HTTP_401_UNAUTHORIZED)

#listar usuarios    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

#deletar usuario
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro': 'o usuario não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({'mensagem': f'usuario {usuario.username} foi deletado com sucesso'}, status=status.HTTP_200_OK)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro': 'O usuário não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

