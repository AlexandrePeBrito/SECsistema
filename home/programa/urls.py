from django.urls import path
from home.programa import views

urlpatterns = [
    # Consultar programas
    path("programa/", views.consultar_programa, name="consultar_programa"),

    # Adicionar novo programa
    path("programa/adicionar/", views.criar_programa, name="adicionar_programa"),

    # Editar programa por ID
    path("programa/editar/<str:id_programa>", views.editar_programa, name="editar_programa"),
]
