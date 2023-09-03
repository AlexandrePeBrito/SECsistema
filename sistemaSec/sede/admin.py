from django.contrib import admin
from .models import Sede

class ListandoSede(admin.ModelAdmin):
    list_display = ("id_sede", "nome_sede", "bairro_sede", "id_municipio_sede")
    list_display_links = ("id_sede", "nome_sede", "bairro_sede")
    search_fields = ("id_sede", "nome_sede", "bairro_sede", "id_municipio_sede__nome_municipio")
    list_per_page: 20
   
admin.site.register(Sede,ListandoSede)