# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from sistemaSec.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('partiu-estagio/dashboard', views.dashboard_partiu_estagio, name='dashboard_partiu_estagio'),
    path('supervisor/dashboard', views.dashboard_supervisor, name='dashboard_supervisor'),
    path('nte/dashboard', views.dashboard_nte, name='dashboard_nte'),
    path('curso/dashboard', views.dashboard_curso, name='dashboard_curso'),
    path('programa/dashboard', views.dashboard_programa, name='dashboard_programa'),
    path('faculdade/dashboard', views.dashboard_faculdade, name='dashboard_faculdade'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
