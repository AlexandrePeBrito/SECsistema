# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.sede import views

urlpatterns  =  [
    path("sede/buscar/", views.consultar_sede, name = "consultar_sede"),
    path("sede/criar/", views.criar_sede, name = "criar_sede"),
    path("sede/editar/<str:id_sede>", views.editar_sede, name = "editar_sede"),
    path("sede/grafico", views.grafico_sede, name = "grafico_sede"),
]