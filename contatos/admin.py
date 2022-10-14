from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome',
                    'data_criacao', 'categoria', 'mostrar', 'telefone')
    # mostra os valores

    list_display_links = ('id', 'nome', 'sobrenome')
    # voce consegue clicar nesses valores e ser levado para o "perfil" dessa pessoa
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')
    # consegue filtrar pelo nome e sobrenome


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
