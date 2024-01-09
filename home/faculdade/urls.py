from django.urls import path
from home.faculdade import views

urlpatterns = [
    path("faculdade/buscar/", views.consultar_faculdade, name="consultar_faculdade"),
    path("faculdade/criar/", views.criar_faculdade, name="criar_faculdade"),
    path("faculdade/editar/<str:id_faculdade>", views.editar_faculdade, name="editar_faculdade"),
]
