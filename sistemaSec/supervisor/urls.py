# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.supervisor import views

urlpatterns = [
    path("supervisor/buscar/", views.consultar_supervisor, name = "consultar_supervisor"),
    path("supervisor/criar/", views.criar_supervisor, name = "criar_supervisor"),
    path("supervisor/editar/<str:id_supervisor>", views.editar_supervisor, name = "editar_supervisor"),
    path("supervisor/grafico", views.grafico_supervisor, name = "grafico_supervisor"),
]