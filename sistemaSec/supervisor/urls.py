# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.supervisor import views

urlpatterns = [
    path("supervisor/buscar/", views.consultar_supervisor, name="consultar_supervisor"),
    path("supervisor/criar/", views.cadastro_supervisor_form, name="cadastro_supervisor_form"),
    path("supervisor/editar/<str:id_supervisor>", views.editar_supervisor, name="editar_supervisor"),
    path("supervisor/atualizar/", views.atualizar_supervisor, name="atualizar_supervisor"),
]