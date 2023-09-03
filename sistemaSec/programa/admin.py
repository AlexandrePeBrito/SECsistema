from django.contrib import admin
from .models import Programa

class ListandoPrograma(admin.ModelAdmin):
    list_display = ("id_programa", "nome_programa")
    list_display_links = ("id_programa", "nome_programa")
    search_fields = ("id_programa","nome_programa")
    list_per_page: 20
   
admin.site.register(Programa,ListandoPrograma)
