# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.edital import views


urlpatterns = [
    path("edital/buscar/", views.consultar_edital, name = "consultar_edital"),
    path("edital/criar/", views.criar_edital, name = "criar_edital"),
    path("edital/editar/<str:id_edital>", views.editar_edital, name = "editar_edital"),
]