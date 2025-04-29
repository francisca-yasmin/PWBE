from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, IngressoSerializer, LoginSerializer
from .permissions import IsGestor, IsGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Ingresso
from rest_framework import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsAuthenticated()]
    #     return [IsGestor]

class IngressoRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.object.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]
    lookup_field = 'pk'

class IngressoListCreateAPIView(ListCreateAPIView):
    queryst = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()] #autenticacao
        return [IsGestor()]