from django.contrib import admin
from app.models import Ingresso, Empresa, Usuario
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields":(
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields":(
                'apelido', 'telefone', 'genero', 'colaborador', 'empresa'
            ),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Ingresso)
admin.site.register(Empresa)