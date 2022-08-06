from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.programa.models import Programa
from .forms import ProgramaForm

url_criar_programa = "home/PROG_criar_programa.html"
url_dashboard_programa = "home/PROG_dashboard.html"
url_editar_programa = "home/PROG_editar_programa.html"

@login_required(login_url = "/login/")
def criar_programa(request):
    form = ProgramaForm(request.POST)

    if request.method == "GET":
        form = ProgramaForm()

        return render(request, url_criar_programa, {"form": form})
    
    else:
        if form.is_valid():
            nome_programa = form.cleaned_data.get("nome_programa")
        
            programa = Programa.objects.create(nome_programa = nome_programa)
            
            programa.save()
            msg = "Programa Cadastrado com Sucesso!"

            return render(request, url_dashboard_programa,cadastrado_programa(form, msg))

        msg = "Ocorreu um ERRO no Cadastro!"
        return render(request, url_dashboard_programa,cadastrado_programa(form, msg))

@login_required(login_url = "/login/")
def consultar_programa(request):
    lista_por_programa = None
    programa = Programa.objects.all()
    
    if "buscar_programa" in request.GET:
        programa_consulta = request.GET["buscar_programa"]
        if consultar_programa:
            lista_por_programa = programa.filter(Q(nome_programa__icontains = programa_consulta))
    
    if lista_por_programa:
        dados = {
            "programas": lista_por_programa,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "programas": lista_por_programa,
            "error": True,
            "mensagem": "Nenhum Programa Localizado!"
        }

    return render(request, url_dashboard_programa,dados)
    
@login_required(login_url = "/login/")    
def editar_programa(request,id_programa):
    programa = Programa.objects.get(id_programa = id_programa)
    form = ProgramaForm(instance = programa)

    edt_programa = { 
        "programa":programa, 
        "form": form }
    
    if request.method == "POST":
        form = ProgramaForm(request.POST, instance = programa)
        if form.is_valid():
            programa.save()

            msg = "Programa Alterado com Sucesso!"
            return render(request,"home/PROG_dashboard.html",cadastrado_programa(form, msg))

        msg = "Ocorreu um erro!"
        return render(request,url_dashboard_programa,cadastrado_programa(form, msg))
    else:
        return render(request, url_editar_programa, edt_programa)

def cadastrado_programa(form, msg):
    programa = Programa.objects.all()
    dados = {
        "programas": programa,
        "form": form,
        "mensagem":msg
    }
    return dados

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
