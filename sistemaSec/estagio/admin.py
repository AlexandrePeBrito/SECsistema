from django.contrib import admin
from .models import Estagio

class ListandoEstagio(admin.ModelAdmin):
    list_display = ("carga_horaria_estagio", "area_estagio", "id_edital_estagio", "id_cursos_estagio")
    list_display_links = ("carga_horaria_estagio", "area_estagio", "id_edital_estagio", "id_cursos_estagio")
    search_fields = ( "area_estagio", "id_edital_estagio__id_edital", "id_cursos_estagio__nome_curso")
    list_per_page: 20
   
admin.site.register(Estagio,ListandoEstagio)