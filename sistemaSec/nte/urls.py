# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.nte import views

urlpatterns = [
    path("nte/buscar/", views.consultar_nte, name = "consultar_nte"),
    path("nte/criar/", views.criar_nte, name = "criar_nte"),
    path("nte/editar/<str:id_NTE>", views.editar_nte, name = "editar_nte"),
]