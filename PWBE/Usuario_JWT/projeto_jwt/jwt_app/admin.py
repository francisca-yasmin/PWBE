from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):

    #o que eu quero ver na pagina da minha aplicação
    list_display = ('username', 'telefone', 'escolaridade', 'endereco', 'bio', 'qtd_animais')
    
    #clicar no usuario especifico, vai mostrar essas informações
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'bio', 'idade')}),
    )

    #quando eu quero criar um usuário novo
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone', 'bio', 'idade')}),
    )

admin.site.register(Usuario, UsuarioAdmin)


