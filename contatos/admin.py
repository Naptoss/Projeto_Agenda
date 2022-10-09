from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'data_criacao', 'categoria')

    list_display_links = ('id', 'nome', 'sobrenome')

    list_filter = ('nome', 'sobrenome')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
