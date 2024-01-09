from django.urls import path
from home.home import views as home_views

urlpatterns = [
    path("", home_views.index, name="home"),
    path("partiu-estagio/dashboard/", home_views.dashboard_estagiario_partiu_estagio, name="dashboard_estagiario_partiu_estagio"),
    path("estagiario/dashboard/", home_views.dashboard_estagiario_mais_futuro, name="dashboard_estagiario_mais_futuro"),
    path("supervisor/dashboard/", home_views.dashboard_supervisor, name="dashboard_supervisor"),
    path("nte/dashboard/", home_views.dashboard_nte, name="dashboard_nte"),
    path("curso/dashboard/", home_views.dashboard_curso, name="dashboard_curso"),
    path("programa/dashboard/", home_views.dashboard_programa, name="dashboard_programa"),
    path("faculdade/dashboard/", home_views.dashboard_faculdade, name="dashboard_faculdade"),
    path("edital/dashboard/", home_views.dashboard_edital, name="dashboard_edital"),
    path("municipio/dashboard/", home_views.dashboard_municipio, name="dashboard_municipio"),
    path("sede/dashboard/", home_views.dashboard_sede, name="dashboard_sede"),
]
