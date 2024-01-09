from django.urls import path
from home.sede import views

urlpatterns = [
    # Buscar sede
    path("sede/buscar/", views.consultar_sede, name="consultar_sede"),

    # Adicionar nova sede
    path("sede/adicionar/", views.criar_sede, name="adicionar_sede"),

    # Atualizar sede por ID
    path("sede/atualizar/<str:id_sede>", views.editar_sede, name="atualizar_sede"),

    # Rota para gráficos da sede
    path("sede/grafico/", views.grafico_sede, name="grafico_sede"),
]
