# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.municipio import views

urlpatterns = [
    path("municipio/buscar/", views.consultar_municipio, name = "consultar_municipio"),
    path("municipio/criar/", views.criar_municipio, name = "criar_municipio"),
    path("municipio/editar/<str:id_municipio>", views.editar_municipio, name = "editar_municipio"),
    path("municipio/grafico", views.grafico_municipio, name = "grafico_municipio"),
]