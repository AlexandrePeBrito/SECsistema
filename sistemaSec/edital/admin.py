from django.contrib import admin
from .models import Edital

class ListandoEdital(admin.ModelAdmin):
    list_display = ("id_edital", "quantidade_vagas_edital")
    list_display_links = ("id_edital", "quantidade_vagas_edital")
    search_fields = ("id_edital", "quantidade_vagas_edital")
    list_per_page: 20
   
admin.site.register(Edital,ListandoEdital)
