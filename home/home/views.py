# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from home.estagiario.models import Estagiario
from home.supervisor.models import Supervisor
from home.nte.models import NTE
from home.curso.models import Curso
from home.programa.models import Programa
from home.faculdade.models import Faculdade
from home.edital.models import Edital
from home.municipio.models import Municipio
from home.sede.models import Sede
from django.db.models import Q

@login_required(login_url="/login/")
def index(request):
    situacao = Estagiario.objects.raw("select 1 as cpf_estagiario, situacao_estagiario as nome , count(cpf_estagiario) as qtd from ESTA_estagiario group by situacao_estagiario")
    sede_bairro = Sede.objects.raw("select 1 as id_sede, bairro_sede as nome, count(id_sede) as qtd from SEDE_sede group by bairro_sede")
    municipio_nte = Municipio.objects.raw("Select 1 as id_municipio, id_NTE as nome, count(id_municipio) as qtd from MUNI_municipio join NTE_nte on NTE_nte.id_NTE = MUNI_municipio.id_nte_municipio_id group by id_NTE")
    supervisor_sede = Supervisor.objects.raw("SELECT 1 AS id_supervisor, nome_sede AS nome, COUNT(id_supervisor) AS qtd, '#ff0000' AS cor FROM SUPE_supervisor JOIN SSES_sede_supervisor_estagiario ON id_supervisor = SSES_id_supervisor_id JOIN SEDE_sede AS sede ON SSES_id_sede_id = id_sede GROUP BY nome_sede")

    context = {
        "segment": "index",
        "situacao": situacao,
        "supervisores": supervisor_sede,
        "sedes": sede_bairro,
        "municipios": municipio_nte,
    }

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template
        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/PAGE_404.html")
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template("home/PAGE_500.html")
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard_estagiario_partiu_estagio(request):
    estagiario = Estagiario.objects.filter(Q(programa_estagiario=4))
    dados = {"estagiarios": estagiario}
    return render(request, "home/PAES_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_estagiario_mais_futuro(request):
    estagiario = Estagiario.objects.filter(Q(programa_estagiario=3))
    dados = {"estagiarios": estagiario}
    return render(request, "home/MFES_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_supervisor(request):
    supervisor = Supervisor.objects.all()
    dados = {"supervisores": supervisor}
    return render(request, "home/SUPE_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_nte(request):
    nte = NTE.objects.all()
    dados = {"NTEs": nte}
    return render(request, "home/NTE_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_curso(request):
    curso = Curso.objects.all()
    dados = {"cursos": curso}
    return render(request, "home/CUSO_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_programa(request):
    programa = Programa.objects.all()
    dados = {"programas": programa}
    return render(request, "home/PROG_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_faculdade(request):
    faculdade = Faculdade.objects.all()
    dados = {"faculdades": faculdade}
    return render(request, "home/FACU_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_edital(request):
    edital = Edital.objects.all()
    dados = {"editais": edital}
    return render(request, "home/EDTL_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_municipio(request):
    municipio = Municipio.objects.all()
    dados = {"municipios": municipio}
    return render(request, "home/MUNI_dashboard.html", dados)

@login_required(login_url="/login/")
def dashboard_sede(request):
    sede = Sede.objects.all()
    dados = {"sedes": sede}
    return render(request, "home/SEDE_dashboard.html", dados)
