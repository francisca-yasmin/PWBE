from django.shortcuts import render
from rest_framework import status
from .models import Usuario, Tarefa
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, TarefaSerializer


class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TarefaListCreate(ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TarefaRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    #mensagens de update
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response ({
            'mensagem': 'a tarefa foi atualizada com sucesso',
            'dados': response.data
        },status=status.HTTP_200_OK)
    
    #mensagem de delete
    def destroy(self, request, *args, **kwargs):
        tarefa = self.get_object()
        self.perform_destroy(tarefa)
        return Response({
            'mensagem': 'tarefa excluida com sucesso'
        }, status=status.HTTP_204_NO_CONTENT)

