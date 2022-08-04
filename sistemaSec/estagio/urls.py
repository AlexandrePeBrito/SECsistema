# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.estagio import views

urlpatterns = [
    path("estagio/buscar/", views.consultar_estagio, name = "consultar_estagio"),
    path("estagio/criar/", views.criar_estagio, name = "criar_estagio"),
    path("estagio/editar/<str:id_estagio>", views.editar_estagio, name = "editar_estagio"),
]