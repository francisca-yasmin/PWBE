from rest_framework.permissions import BasePermission

#permissao personalizada
class IsGestor(BasePermission):
    def has_permission(self, request, view): #permissão geral
        return request.user.is_authenticated and request.user.colaborador == 'G'
    
class IsGestorOuDono(BasePermission):
    def has_object_permission(self, request, view, obj): #permissao para acessar um objeto (especifico)
        if request.user.colaborador == 'G':
            return True #se for gestor ele pode alterar
        return obj.usuario == request.user #verifica se eh usuario
        