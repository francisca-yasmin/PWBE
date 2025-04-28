from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.criar_user, name='criar_user'), #funciona
    path('logar/', view=views.logar_user, name='logar_usuario'), #funciona
    path('read/', view=views.read, name='read'), #funciona
    path('deletar/<int:pk>', view=views.delete_user, name='delete_user'), #funciona
    path('atualizar/<int:pk>', view=views.update_user, name='update_user') #funciona
]