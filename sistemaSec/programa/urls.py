# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.programa import views

urlpatterns = [
    path("programa/buscar/", views.consultar_programa, name="consultar_programa"),
    path("programa/criar/", views.criar_programa, name="criar_programa"),
    path("programa/editar/<str:id_programa>", views.editar_programa, name="editar_programa"),
]