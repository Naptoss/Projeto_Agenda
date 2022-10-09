from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'data_criacao', 'categoria')
    # mostra os valores

    list_display_links = ('id', 'nome', 'sobrenome')
    # voce consegue clicar nesses valores e ser levado para o "perfil" dessa pessoa

    list_filter = ('nome', 'sobrenome')

    # consegue filtrar pelo nome e sobrenome


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
