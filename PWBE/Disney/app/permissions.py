from rest_framework.permissions import BasePermission

#permissao personalizada
class IsGestor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.colaborador == 'G'
    