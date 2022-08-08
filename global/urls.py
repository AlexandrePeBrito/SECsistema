# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    
    path("admin/", admin.site.urls),          # Django admin route
    path("", include("sistemaSec.autenticacao.urls")),    # Auth routes - login / register
    path("", include("sistemaSec.estagiario.urls")),
    path("", include("sistemaSec.supervisor.urls")),
    path("", include("sistemaSec.nte.urls")),
    path("", include("sistemaSec.curso.urls")),
    path("", include("sistemaSec.programa.urls")),
    path("", include("sistemaSec.faculdade.urls")),
    path("", include("sistemaSec.edital.urls")),
    path("", include("sistemaSec.municipio.urls")),
    path("", include("sistemaSec.sede.urls")),
    path("", include("sistemaSec.home.urls"))            # UI Kits Html files
]
