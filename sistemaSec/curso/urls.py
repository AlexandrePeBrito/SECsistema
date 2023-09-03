# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.curso import views

urlpatterns = [
    path("curso/buscar/", views.consultar_curso, name = "consultar_curso"),
    path("curso/criar/", views.criar_curso, name = "criar_curso"),
    path("curso/editar/<str:id_curso>", views.editar_curso, name = "editar_curso"),
]