from django.urls import path
from home.supervisor import views

urlpatterns = [
    # Buscar supervisor
    path("supervisor/buscar/", views.consultar_supervisor, name="consultar_supervisor"),

    # Criar supervisor
    path("supervisor/criar/", views.criar_supervisor, name="criar_supervisor"),

    # Editar supervisor por ID
    path("supervisor/editar/<str:id_supervisor>", views.editar_supervisor, name="editar_supervisor"),

    # Rota para gráficos do supervisor
    path("supervisor/grafico/", views.grafico_supervisor, name="grafico_supervisor"),
]
