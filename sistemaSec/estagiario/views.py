# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import re
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re
from sistemaSec.edital.models import Edital
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.programa.models import Programa
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.sede.models import Sede
from sistemaSec.estagio.models import Estagio
from sistemaSec.faculdade.models import Faculdade
from .forms import EstagiarioForm
from django.forms.models import model_to_dict

url_criar_estagiario_partiu_estagio = "home/PAES_criar_estagiario.html"
url_dashboard_estagiario_partiu_estagio = "home/PAES_dashboard.html"
url_editar_estagiario_partiu_estagio = "home/PAES_editar_estagiario.html"

@login_required(login_url = "/login/")
def criar_estagiario_partiu_estagio(request):
    form = EstagiarioForm(request.POST)

    if request.method == "GET":
        form = EstagiarioForm()

        return render(request, url_criar_estagiario_partiu_estagio, {"form": form})
    else:
        if form.is_valid():
            nome_estagiario = form.cleaned_data.get("nome_estagiario")
            cpf = form.cleaned_data.get("cpf_estagiario")
            rg = form.cleaned_data.get("rg_estagiario")
            turno = form.cleaned_data.get("turno_estagiario")
            email = form.cleaned_data.get("email_estagiario")
            semestre = form.cleaned_data.get("semestre_estagiario")
            nis = form.cleaned_data.get("nis_pis_estagiario")
            telefone = form.cleaned_data.get("telefone_estagiario")
            responsavel = form.cleaned_data.get("nome_responsavel_estagiario")
            nascimento = form.cleaned_data.get("data_nascimento_estagiario")
            genero = form.cleaned_data.get("genero_estagiario")
            raca = form.cleaned_data.get("raca_estagiario")
            bairro = form.cleaned_data.get("bairro_estagiario")
            numero = form.cleaned_data.get("numero_estagiario")
            complemento = form.cleaned_data.get("complemento_estagiario")
            matricula = form.cleaned_data.get("matricula_estagiario")
            situacao = form.cleaned_data.get("situacao_estagiario")
            supervisor = form.cleaned_data.get("supervisor_estagiario")
            sede = form.cleaned_data.get("sede_estagiario")
            faculdade = form.cleaned_data.get("faculdade_estagiario")
            estagio = form.cleaned_data.get("estagio_estagiario")

            estagiario = Estagiario.objects.create(cpf_estagiario = cpf,
                nome_estagiario = nome_estagiario, rg_estagiario = rg,
                turno_estagiario = turno, email_estagiario = email,
                semestre_estagiario = semestre, nis_pis_estagiario = nis,
                telefone_estagiario = telefone, nome_responsavel_estagiario = responsavel,
                data_nascimento_estagiario = nascimento,
                genero_estagiario = genero, raca_estagiario = raca,
                bairro_estagiario = bairro, numero_estagiario = numero,
                complemento_estagiario = complemento, matricula_estagiario = matricula,
                situacao_estagiario = situacao, supervisor_estagiario = supervisor,
                sede_estagiario = sede, faculdade_estagiario = faculdade,
                estagio_estagiario = estagio)
            
            estagiario.save()
            msg = "Estagiario Cadastrado com Sucesso!"
            return render(request, url_dashboard_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, msg))
        
        print(form.errors)
        msg = "Ocorreu um Error!"
        return render(request, url_dashboard_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, msg))

@login_required(login_url = "/login/")
def consultar_estagiario_partiu_estagio(request):
    
    estagiarios = Estagiario.objects.all()
    
        
    if "buscar_estagiario_partiu_estagio" in request.GET:
        nome_consulta=request.GET["buscar_estagiario_partiu_estagio"]
        cpf_consulta=request.GET["buscar_cpf_estagiario_partiu_estagio"]
        situacao_consulta=request.GET["buscar_situacao_estagiario_partiu_estagio"]
        turno_consulta=request.GET["buscar_turno_estagiario_partiu_estagio"]
        bairro_consulta=request.GET["buscar_bairro_estagiario_partiu_estagio"]
        supervisor_consulta=request.GET["buscar_supervisor_estagiario_partiu_estagio"]
        sede_consulta=request.GET["buscar_sede_estagiario_partiu_estagio"]
        faculdade_consulta=request.GET["buscar_faculdade_estagiario_partiu_estagio"]

        if consultar_estagiario_partiu_estagio:
            lista_por_nome = estagiarios.filter(Q(nome_estagiario__icontains=nome_consulta))
            lista_por_cpf = lista_por_nome.filter(Q(cpf_estagiario__icontains=cpf_consulta))
            lista_por_situacao = lista_por_cpf.filter(Q(situacao_estagiario__icontains=situacao_consulta))
            lista_por_turno = lista_por_situacao.filter(Q(turno_estagiario__icontains=turno_consulta))
            lista_por_bairro = lista_por_turno.filter(Q(bairro_estagiario__icontains=bairro_consulta))
            lista_por_supervisor = lista_por_bairro.filter(Q(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta))
            lista_por_sede = lista_por_supervisor.filter(Q(sede_estagiario__nome_sede__icontains=sede_consulta))
            lista_por_faculdade = lista_por_sede.filter(Q(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta))
            lista_partiu_estagio = lista_por_faculdade.filter(Q(estagio_estagiario=1))

    
    if lista_partiu_estagio:
        dados = {
            "estagiarios": lista_partiu_estagio,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "estagiarios": lista_partiu_estagio,
            "error": True,
            "mensagem": "Nenhum Estagiario Localizado!"
        }
    
    return render(request, url_dashboard_estagiario_partiu_estagio, dados)
    
@login_required(login_url = "/login/")    
def editar_estagiario_partiu_estagio(request, cpf_estagiario):
    estagiario = Estagiario.objects.get(cpf_estagiario = cpf_estagiario)
    form = EstagiarioForm(initial = model_to_dict(estagiario))

    editar_estagiario_partiu_estagio = { 
        "estagiario":estagiario,
        "form": form }

    if request.method == "POST":
        form = EstagiarioForm(request.POST, instance = estagiario)

        if form.is_valid():
            estagiario.save()

            msg = "Estagiario Alterado com sucesso!"
            return render(request, url_dashboard_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, msg))
        
        print(form.errors)
        msg = "Ocorreu um Erro"
        return render(request, url_dashboard_estagiario_partiu_estagio, cadastrado_estagiario_partiu_estagio(form, msg))
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

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

def is_choice_empty(campo):
    if campo == 0:
        return False
    else:
        return True

def cadastrado_estagiario_partiu_estagio(form, msg):
    programa_consulta = get_object_or_404(Programa,id_programa = 1)
    sede_consulta = Edital.objects.filter(id_programa_edital_id = programa_consulta)
    estagio = Estagio.objects.filter(id_edital_estagio_id__in = sede_consulta)
    estagiario = Estagiario.objects.filter(estagio_estagiario_id__in = estagio)
    
    dados ={
        "estagiarios": estagiario,
        "form": form,
        "mensagem":msg
    }
   
    return dados


def cadastrado_estagiario_mais_futuro(form, msg):
    programa_consulta = get_object_or_404(Programa,id_programa = 2)
    sede_consulta = Edital.objects.filter(id_programa_edital_id = programa_consulta)
    estagio = Estagio.objects.filter(id_edital_estagio_id__in = sede_consulta)
    estagiario = Estagiario.objects.filter(estagio_estagiario_id__in = estagio)
    
    dados ={
        "estagiarios": estagiario,
        "form": form,
        "mensagem":msg
    }
   
    return dados

url_criar_estagiario_mais_futuro = "home/MFES_criar_estagiario.html"
url_dashboard_estagiario_mais_futuro = "home/MFES_dashboard.html"
url_editar_estagiario_mais_futuro = "home/MFES_editar_estagiario.html"


@login_required(login_url="/login/")
def criar_estagiario_mais_futuro(request):
    form = EstagiarioForm(request.POST)

    if request.method == "GET":
        form = EstagiarioForm()

        return render(request, url_criar_estagiario_mais_futuro, {"form": form})
    else:
        if form.is_valid():
            nome_estagiario = form.cleaned_data.get("nome_estagiario")
            cpf = form.cleaned_data.get("cpf_estagiario")
            rg = form.cleaned_data.get("rg_estagiario")
            turno = form.cleaned_data.get("turno_estagiario")
            email = form.cleaned_data.get("email_estagiario")
            semestre = form.cleaned_data.get("semestre_estagiario")
            nis = form.cleaned_data.get("nis_pis_estagiario")
            telefone = form.cleaned_data.get("telefone_estagiario")
            responsavel = form.cleaned_data.get("nome_responsavel_estagiario")
            nascimento = form.cleaned_data.get("data_nascimento_estagiario")
            genero = form.cleaned_data.get("genero_estagiario")
            raca = form.cleaned_data.get("raca_estagiario")
            bairro = form.cleaned_data.get("bairro_estagiario")
            numero = form.cleaned_data.get("numero_estagiario")
            complemento = form.cleaned_data.get("complemento_estagiario")
            matricula = form.cleaned_data.get("matricula_estagiario")
            situacao = form.cleaned_data.get("situacao_estagiario")
            supervisor = form.cleaned_data.get("supervisor_estagiario")
            sede = form.cleaned_data.get("sede_estagiario")
            faculdade = form.cleaned_data.get("faculdade_estagiario")
            estagio = form.cleaned_data.get("estagio_estagiario")

            estagiario = Estagiario.objects.create(cpf_estagiario = cpf,
                nome_estagiario = nome_estagiario, rg_estagiario = rg,
                turno_estagiario = turno, email_estagiario = email,
                semestre_estagiario = semestre, nis_pis_estagiario = nis,
                telefone_estagiario = telefone, nome_responsavel_estagiario = responsavel,
                data_nascimento_estagiario = nascimento,
                genero_estagiario = genero, raca_estagiario = raca,
                bairro_estagiario = bairro, numero_estagiario = numero,
                complemento_estagiario = complemento, matricula_estagiario = matricula,
                situacao_estagiario = situacao, supervisor_estagiario = supervisor,
                sede_estagiario = sede, faculdade_estagiario = faculdade,
                estagio_estagiario = estagio)
            
            estagiario.save()
            msg = "Estagiario Cadastrado com Sucesso!"
            return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg))
        
        print(form.errors)
        msg = "Ocorreu um Error!"
        return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg))

@login_required(login_url="/login/")
def consultar_estagiario_mais_futuro(request):
    
    estagiarios = Estagiario.objects.all()
    
        
    if "buscar_estagiario_partiu_estagio" in request.GET:
        nome_consulta=request.GET["buscar_estagiario_partiu_estagio"]
        cpf_consulta=request.GET["buscar_cpf_estagiario_partiu_estagio"]
        situacao_consulta=request.GET["buscar_situacao_estagiario_partiu_estagio"]
        turno_consulta=request.GET["buscar_turno_estagiario_partiu_estagio"]
        bairro_consulta=request.GET["buscar_bairro_estagiario_partiu_estagio"]
        supervisor_consulta=request.GET["buscar_supervisor_estagiario_partiu_estagio"]
        sede_consulta=request.GET["buscar_sede_estagiario_partiu_estagio"]
        faculdade_consulta=request.GET["buscar_faculdade_estagiario_partiu_estagio"]

        if consultar_estagiario_mais_futuro:
            lista_por_nome = estagiarios.filter(Q(nome_estagiario__icontains=nome_consulta))
            lista_por_cpf = lista_por_nome.filter(Q(cpf_estagiario__icontains=cpf_consulta))
            lista_por_situacao = lista_por_cpf.filter(Q(situacao_estagiario__icontains=situacao_consulta))
            lista_por_turno = lista_por_situacao.filter(Q(turno_estagiario__icontains=turno_consulta))
            lista_por_bairro = lista_por_turno.filter(Q(bairro_estagiario__icontains=bairro_consulta))
            lista_por_supervisor = lista_por_bairro.filter(Q(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta))
            lista_por_sede = lista_por_supervisor.filter(Q(sede_estagiario__nome_sede__icontains=sede_consulta))
            lista_por_faculdade = lista_por_sede.filter(Q(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta))
            lista_mais_futuro = lista_por_faculdade.filter(Q(estagio_estagiario=2))

    if lista_mais_futuro:
        dados = {
            "estagiarios": lista_mais_futuro,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "estagiarios": lista_mais_futuro,
            "error": True,
            "mensagem": "Nenhum Estagiario Localizado!"
        }

    return render(request, url_dashboard_estagiario_mais_futuro, dados)
    
@login_required(login_url="/login/")    
def editar_estagiario_mais_futuro(request,cpf_estagiario):
    estagiario = Estagiario.objects.get(cpf_estagiario=cpf_estagiario)
    form = EstagiarioForm(initial = model_to_dict(estagiario))

    editar_estagiario_partiu_estagio = { 
        "estagiario":estagiario,
        "form": form }

    if request.method == "POST":
        form = EstagiarioForm(request.POST, instance = estagiario)

        if form.is_valid():
            estagiario.save()

            msg = "Estagiario Alterado com sucesso!"
            return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg))
        
        print(form.errors)
        msg = "Ocorreu um Erro"
        return render(request, url_dashboard_estagiario_mais_futuro, cadastrado_estagiario_mais_futuro(form, msg))
    else:    
        return render(request, url_editar_estagiario_mais_futuro, editar_estagiario_partiu_estagio)
    


