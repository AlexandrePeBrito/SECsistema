from django.urls import path
from home.nte import views

urlpatterns = [
    # Consultar NTEs
    path("nte/", views.consultar_nte, name="consultar_nte"),

    # Adicionar novo NTE
    path("nte/adicionar/", views.criar_nte, name="adicionar_nte"),

    # Editar NTE por ID
    path("nte/editar/<str:id_NTE>", views.editar_nte, name="editar_nte"),
]
