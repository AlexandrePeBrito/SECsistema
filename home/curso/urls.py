from django.urls import path
from home.curso import views

urlpatterns = [
    # Consultar cursos
    path("curso/buscar/", views.consultar_curso, name="consultar_curso"),

    # Criar curso
    path("curso/criar/", views.criar_curso, name="criar_curso"),

    # Editar curso
    path("curso/editar/<str:id_curso>/", views.editar_curso, name="editar_curso"),
]
