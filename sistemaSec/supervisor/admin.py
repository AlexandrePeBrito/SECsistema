from django.contrib import admin
from .models import Supervisor

class ListandoSupervisor(admin.ModelAdmin):
    list_display = ("id_supervisor", "nome_supervisor")
    list_display_links = ("id_supervisor", "nome_supervisor")
    search_fields = ("nome_supervisor",)
    list_per_page: 20
   
admin.site.register(Supervisor,ListandoSupervisor)