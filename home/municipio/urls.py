from django.urls import path
from home.municipio import views

urlpatterns = [
    path("municipios/", views.consultar_municipio, name="consultar_municipios"),
    path("municipios/adicionar/", views.criar_municipio, name="adicionar_municipio"),
    path("municipios/editar/<str:id_municipio>", views.editar_municipio, name="editar_municipio"),
    path("municipios/grafico/", views.grafico_municipio, name="grafico_municipio"),
]
