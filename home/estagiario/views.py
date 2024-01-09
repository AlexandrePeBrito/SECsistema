# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from home.estagiario.models import Estagiario
from .forms import EstagiarioForm
from django.forms.models import model_to_dict
import re

url_criar_estagiario_partiu_estagio = "home/PAES_criar_estagiario.html"
url_dashboard_estagiario_partiu_estagio = "home/PAES_dashboard.html"
url_editar_estagiario_partiu_estagio = "home/PAES_editar_estagiario.html"

@login_required(login_url="/login/")
def grafico_estagiario_partiu_estagio(request):
    genero = Estagiario.objects.raw("select 1 as cpf_estagiario, genero_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 4 group by genero_estagiario")
    raca = Estagiario.objects.raw("select 1 as cpf_estagiario, raca_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 4 group by raca_estagiario")
    turno = Estagiario.objects.raw("select 1 as cpf_estagiario, turno_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 4 group by turno_estagiario")
    situacao = Estagiario.objects.raw("select 1 as cpf_estagiario, situacao_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 4 group by situacao_estagiario")
    
    cores = ["#ed0919", "#2a07f0", "#b33062", "#5652c7", "#ed0919", "#2a07f0", "#b33062", "#5652c7"]
    i = 0
    for g in genero:
        g.cor = cores[i]
        i += 1
    i = 0
    for r in raca:
        r.cor = cores[i]
        i += 1
    i = 0
    for t in turno:
        t.cor = cores[i]
        i += 1
    i = 0
    for s in situacao:
        s.cor = cores[i]
        i += 1

    grafico = {
        "generos": genero,
        "racas": raca,
        "turnos": turno,
        "situacao": situacao,
    }
    return render(request, "home/PAES_grafico.html", grafico)

@login_required(login_url="/login/")
def criar_estagiario_partiu_estagio(request):
    form = EstagiarioForm(request.POST or None)

    if request.method == "GET":
        form = EstagiarioForm()

        return render(request, url_criar_estagiario_partiu_estagio, {"form": form})
    else:
        if form.is_valid():
            estagiario = form.save(commit=False)
            estagiario.programa_estagiario_id = 4  # Definir o programa diretamente

            estagiario.save()
            msg = "Estagiario Cadastrado com Sucesso!"
            return render(request, url_dashboard_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, msg, False))
        
        return render(request, url_criar_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, form.errors, True))

@login_required(login_url="/login/")
def consultar_estagiario_partiu_estagio(request):
    todos_estagiario = Estagiario.objects.filter(programa_estagiario=4)  # Filtrar diretamente

    if request.method == "GET":
        nome_consulta = request.GET.get("buscar_estagiario_partiu_estagio", "")
        cpf_consulta = request.GET.get("buscar_cpf_estagiario_partiu_estagio", "")
        situacao_consulta = request.GET.get("buscar_situacao_estagiario_partiu_estagio", "")
        turno_consulta = request.GET.get("buscar_turno_estagiario_partiu_estagio", "")
        bairro_consulta = request.GET.get("buscar_bairro_estagiario_partiu_estagio", "")
        supervisor_consulta = request.GET.get("buscar_supervisor_estagiario_partiu_estagio", "")
        sede_consulta = request.GET.get("buscar_sede_estagiario_partiu_estagio", "")
        faculdade_consulta = request.GET.get("buscar_faculdade_estagiario_partiu_estagio", "")
        curso_consulta = request.GET.get("buscar_curso_estagiario_partiu_estagio", "")
        edital_consulta = request.GET.get("buscar_edital_estagiario_partiu_estagio", "")

        if nome_consulta or cpf_consulta or situacao_consulta or turno_consulta or bairro_consulta or supervisor_consulta or sede_consulta or faculdade_consulta or curso_consulta or edital_consulta:
            query = Q()
            if nome_consulta:
                query &= Q(nome_estagiario__icontains=nome_consulta)
            if cpf_consulta:
                query &= Q(cpf_estagiario__icontains=cpf_consulta)
            if situacao_consulta:
                query &= Q(situacao_estagiario__icontains=situacao_consulta)
            if turno_consulta:
                query &= Q(turno_estagiario__icontains=turno_consulta)
            if bairro_consulta:
                query &= Q(bairro_estagiario__icontains=bairro_consulta)
            if supervisor_consulta:
                query &= Q(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta)
            if sede_consulta:
                query &= Q(sede_estagiario__nome_sede__icontains=sede_consulta)
            if faculdade_consulta:
                query &= Q(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta)
            if curso_consulta:
                query &= Q(curso_estagiario__nome_curso__icontains=curso_consulta)
            if edital_consulta:
                query &= Q(edital_estagiario__id_edital__icontains=edital_consulta)

            lista_por_edital = todos_estagiario.filter(query)

    if lista_por_edital:
        dados = {
            "estagiarios": lista_por_edital,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "estagiarios": lista_por_edital,
            "error": True,
            "mensagem": "Nenhum Estagiario Localizado!"
        }
    
    return render(request, url_dashboard_estagiario_partiu_estagio, dados)


@login_required(login_url="/login/")
def editar_estagiario_partiu_estagio(request, cpf_estagiario):
    estagiario = Estagiario.objects.get(cpf_estagiario=cpf_estagiario)
    form = EstagiarioForm(initial=model_to_dict(estagiario))
    editar_estagiario_partiu_estagio = {"estagiario": estagiario, "form": form}

    if request.method == "POST":
        form = EstagiarioForm(request.POST, instance=estagiario)

        if form.is_valid():
            estagiario.save()
            msg = "Estagiario Alterado com sucesso!"
            return render(
                request,
                url_dashboard_estagiario_partiu_estagio,
                cadastrado_estagiario_partiu_estagio(form, msg, False),
            )
        
        return render(
            request,
            url_editar_estagiario_partiu_estagio,
            cadastrado_estagiario_partiu_estagio(form, form.errors, True),
        )
    else:
        return render(request, url_editar_estagiario_partiu_estagio, editar_estagiario_partiu_estagio)



def is_cpf_valid(cpf):
     # Check if type is str
    if not isinstance(cpf,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]","",cpf)
    
    # Verify if CPF number is equal
    if cpf=="00000000000" or cpf == "11111111111" or cpf == "22222222222" or cpf == "33333333333" or cpf == "44444444444" or cpf == "55555555555" or cpf == "66666666666" or cpf == "77777777777" or cpf == "88888888888" or cpf == "99999999999":
        return False

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 -  sum % 11

    if verifying_digit > 9 :
        first_verifying_digit = 0
    else:
        first_verifying_digit = verifying_digit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 -  sum % 11

    if verifying_digit > 9 :
        second_verifying_digit = 0
    else:
        second_verifying_digit = verifying_digit

    if cpf[-2:] == "%s%s" % (first_verifying_digit,second_verifying_digit):
        return True
    return False

def is_empty(campo):
    if campo == 0:
        return True
    else:
        return False

def is_choice_empty(campo):
    if campo == 0:
        return False
    else:
        return True

def cadastrado_estagiario_partiu_estagio(form, msg, error):
    todos_estagiario = Estagiario.objects.all()
    estagiario = todos_estagiario.filter(Q(programa_estagiario = 4))
 
    
    dados ={
        "estagiarios": estagiario,
        "form": form,
        "error": error,
        "mensagem":msg
    }
   
    return dados

def cadastrado_estagiario_mais_futuro(form, msg, error):
    todos_estagiario = Estagiario.objects.all()
    estagiario = todos_estagiario.filter(Q(programa_estagiario = 3))
    
    dados ={
        "estagiarios": estagiario,
        "form": form,
        "error": error,
        "mensagem":msg
    }
   
    return dados

url_criar_estagiario_mais_futuro = "home/MFES_criar_estagiario.html"
url_dashboard_estagiario_mais_futuro = "home/MFES_dashboard.html"
url_editar_estagiario_mais_futuro = "home/MFES_editar_estagiario.html"

def grafico_estagiario_mais_futuro(request):
    genero = Estagiario.objects.raw("select 1 as cpf_estagiario, genero_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 3 group by genero_estagiario")
    raca = Estagiario.objects.raw("select 1 as cpf_estagiario, raca_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 3 group by raca_estagiario")
    turno = Estagiario.objects.raw("select 1 as cpf_estagiario, turno_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 3 group by turno_estagiario")
    situacao = Estagiario.objects.raw("select 1 as cpf_estagiario, situacao_estagiario as nome , count(cpf_estagiario) as qtd, '#ff0000' as cor from ESTA_estagiario where programa_estagiario_id = 3 group by situacao_estagiario")
    
    cores = ["#ed0919", "#2a07f0", "#b33062", "#5652c7", "#ed0919", "#2a07f0", "#b33062", "#5652c7"]
    #"#1de9b6", "#A389D4", "#04a9f5", 
    i = 0
    for g in genero:
        g.cor = cores[i]
        i = i + 1
    i = 0
    for r in raca:
        r.cor = cores[i]
        i = i + 1
    i = 0
    for t in turno:
        t.cor = cores[i]
        i = i + 1
    i = 0
    for s in situacao:
        s.cor = cores[i]
        i = i + 1

    grafico ={
        "generos": genero,
        "racas": raca,
        "turnos": turno,
        "situacao": situacao,
    }
    return render(request, "home/MFES_grafico.html", grafico)

@login_required(login_url="/login/")
def criar_estagiario_mais_futuro(request):
    form = EstagiarioForm(request.POST if request.method == "POST" else None)

    if request.method == "GET" or not form.is_valid():
        form = EstagiarioForm()

    if form.is_valid():
        estagiario = form.save(commit=False)
        msg = "Estagiario Cadastrado com Sucesso!"
        estagiario.save()
        return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg, False))

    return render(request, url_criar_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, form.errors, True))

@login_required(login_url="/login/")
def consultar_estagiario_mais_futuro(request):
    todos_estagiario = Estagiario.objects.filter(programa_estagiario=3)
    
    if "buscar_estagiario_partiu_estagio" in request.GET:
        nome_consulta = request.GET.get("buscar_estagiario_partiu_estagio")
        cpf_consulta = request.GET.get("buscar_cpf_estagiario_partiu_estagio")
        situacao_consulta = request.GET.get("buscar_situacao_estagiario_partiu_estagio")
        turno_consulta = request.GET.get("buscar_turno_estagiario_partiu_estagio")
        bairro_consulta = request.GET.get("buscar_bairro_estagiario_partiu_estagio")
        supervisor_consulta = request.GET.get("buscar_supervisor_estagiario_partiu_estagio")
        sede_consulta = request.GET.get("buscar_sede_estagiario_partiu_estagio")
        faculdade_consulta = request.GET.get("buscar_faculdade_estagiario_partiu_estagio")
        curso_consulta = request.GET.get("buscar_curso_estagiario_partiu_estagio")
        edital_consulta = request.GET.get("buscar_edital_estagiario_partiu_estagio")

        lista_por_nome = todos_estagiario.filter(nome_estagiario__icontains=nome_consulta)
        lista_por_cpf = lista_por_nome.filter(cpf_estagiario__icontains=cpf_consulta)
        lista_por_situacao = lista_por_cpf.filter(situacao_estagiario__icontains=situacao_consulta)
        lista_por_turno = lista_por_situacao.filter(turno_estagiario__icontains=turno_consulta)
        lista_por_bairro = lista_por_turno.filter(bairro_estagiario__icontains=bairro_consulta)
        lista_por_supervisor = lista_por_bairro.filter(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta)
        lista_por_sede = lista_por_supervisor.filter(sede_estagiario__nome_sede__icontains=sede_consulta)
        lista_por_faculdade = lista_por_sede.filter(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta)
        lista_por_curso = lista_por_faculdade.filter(curso_estagiario__nome_curso__icontains=curso_consulta)
        lista_por_edital = lista_por_curso.filter(edital_estagiario__id_edital__icontains=edital_consulta)

        dados = {
            "estagiarios": lista_por_edital,
            "error": False if lista_por_edital else True,
            "mensagem": "Consulta Feita com Sucesso!" if lista_por_edital else "Nenhum Estagiario Localizado!"
        }

        return render(request, url_dashboard_estagiario_mais_futuro, dados)

    return render(request, url_dashboard_estagiario_mais_futuro, {"estagiarios": todos_estagiario})

@login_required(login_url="/login/")    
def editar_estagiario_mais_futuro(request, cpf_estagiario):
    estagiario = Estagiario.objects.get(cpf_estagiario=cpf_estagiario)
    form = EstagiarioForm(request.POST or None, instance=estagiario)

    editar_estagiario_partiu_estagio = { 
        "estagiario": estagiario,
        "form": form
    }

    if request.method == "POST" and form.is_valid():
        form.save()
        msg = "Estagiario Alterado com sucesso!"
        return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg, False))
        
    return render(request, url_editar_estagiario_mais_futuro, editar_estagiario_partiu_estagio)
