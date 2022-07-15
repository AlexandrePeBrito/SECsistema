# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.estagiario import views

urlpatterns = [
    path("partiu-estagio/buscar/", views.consultar_estagiario_partiu_estagio, name="consultar_estagiario_partiu_estagio"),
    path("partiu-estagio/criar/", views.criar_estagiario_partiu_estagio, name="criar_estagiario_partiu_estagio"),
    path("partiu-estagio/editar/<str:cpf_estagiario>", views.editar_estagiario_partiu_estagio, name="editar_estagiario_partiu_estagio"),
    path("partiu-estagio/atualizar/", views.atualizar_estagiario_partiu_estagio, name="atualizar_estagiario_partiu_estagio"),
]