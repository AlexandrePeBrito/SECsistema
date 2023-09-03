from django.contrib import admin
from .models import Municipio

class ListandoEdital(admin.ModelAdmin):
    list_display = ("id_municipio", "nome_municipio", "id_nte_municipio")
    list_display_links = ("id_municipio", "nome_municipio", "id_nte_municipio")
    search_fields = ("id_municipio", "nome_municipio", "id_nte_municipio__id_NTE")
    list_per_page: 20
   
admin.site.register(Municipio,ListandoEdital)