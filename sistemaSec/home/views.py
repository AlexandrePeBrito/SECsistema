# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.nte.models import NTE
from sistemaSec.curso.models import Curso
from sistemaSec.programa.models import Programa
from sistemaSec.faculdade.models import Faculdade
from sistemaSec.edital.models import Edital
from sistemaSec.municipio.models import Municipio
from sistemaSec.sede.models import Sede

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        print('CAMINHO AQUI '+load_template)
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/PAGE_404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/PAGE_500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard_partiu_estagio(request):
    estagiario = Estagiario.objects.all()
    dados ={
        'estagiarios': estagiario
    }
    return render(request, 'home/PAES_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_supervisor(request):
    supervisor = Supervisor.objects.all()
    dados ={
        'supervisores': supervisor
    }
    return render(request, 'home/SUPE_dashboard.html',dados)


@login_required(login_url="/login/")
def dashboard_nte(request):
    nte = NTE.objects.all()
    dados ={'NTEs': nte}
    return render(request, 'home/NTE_dashboard.html',dados)


@login_required(login_url="/login/")
def dashboard_curso(request):
    curso = Curso.objects.all()
    dados ={'cursos': curso}
    return render(request, 'home/CUSO_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_programa(request):
    programa = Programa.objects.all()
    dados ={'programas': programa}
    return render(request, 'home/PROG_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_faculdade(request):
    faculdade = Faculdade.objects.all()
    dados ={'faculdades': faculdade}
    return render(request, 'home/FACU_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_edital(request):
    edital = Edital.objects.all()
    dados ={'editais': edital}
    return render(request, 'home/EDTL_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_municipio(request):
    municipio = Municipio.objects.all()
    dados ={'municipios': municipio}
    return render(request, 'home/MUNI_dashboard.html',dados)

@login_required(login_url="/login/")
def dashboard_sede(request):
    sede = Sede.objects.all()
    dados ={'sedes': sede}
    return render(request, 'home/SEDE_dashboard.html',dados)
