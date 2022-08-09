# -*- encoding: utf-8 -*-
from django.urls import path
from sistemaSec.estagiario import views

urlpatterns = [
    #   Partiu Estagio
    path("partiu-estagio/buscar/", views.consultar_estagiario_partiu_estagio, name = "consultar_estagiario_partiu_estagio"),
    path("partiu-estagio/criar/", views.criar_estagiario_partiu_estagio, name = "criar_estagiario_partiu_estagio"),
    path("partiu-estagio/editar/<str:cpf_estagiario>", views.editar_estagiario_partiu_estagio, name = "editar_estagiario_partiu_estagio"),
    path("partiu-estagio/grafico/", views.grafico_estagiario_partiu_estagio, name = "grafico_estagiario_partiu_estagio"),
    #   Mais Futuro
    path("mais-futuro/buscar/", views.consultar_estagiario_mais_futuro, name = "consultar_estagiario_mais_futuro"),
    path("mais-futuro/criar/", views.criar_estagiario_mais_futuro, name = "criar_estagiario_mais_futuro"),
    path("mais-futuro/editar/<str:cpf_estagiario>", views.editar_estagiario_mais_futuro, name = "editar_estagiario_mais_futuro"),
    path("mais-futuro/grafico", views.grafico_estagiario_mais_futuro, name = "grafico_estagiario_mais_futuro"),
]