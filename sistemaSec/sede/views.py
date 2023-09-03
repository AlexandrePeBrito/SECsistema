from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.sede.models import Sede
from .forms import SedeForm
from django.forms.models import model_to_dict

url_criar_sede ="home/SEDE_criar_sede.html"
url_dashboard_sede = "home/SEDE_dashboard.html"
url_editar_sede = "home/SEDE_editar_sede.html"

@login_required(login_url = "/login/")
def grafico_sede(request):
    municipio = Sede.objects.raw("select 1 as id_sede, nome_municipio as nome, count(id_sede) as qtd, '#ff0000' as cor from sede_sede right join muni_municipio on id_municipio_sede_id = id_municipio group by nome_municipio LIMIT 20")
    nte = Sede.objects.raw("select 1 as id_sede, id_NTE as nome, COUNT(id_sede) as qtd, '#ff0000' as cor FROM nte_nte LEFT JOIN muni_municipio ON id_nte_municipio_id = id_NTE LEFT JOIN sede_sede ON id_municipio_sede_id = id_municipio GROUP BY id_NTE")
    bairro = Sede.objects.raw("select 1 as id_sede, bairro_sede as nome, count(id_sede) as qtd, '#ff0000' as cor from sede_sede group by bairro_sede LIMIT 20")

    cores = ["#ed0919", "#2a07f0", "#b33062", "#5652c7", "#ed0919", "#2a07f0", "#b33062", "#5652c7"]
    #"#1de9b6", "#A389D4", "#04a9f5", 

    i = 0
    for m in municipio:
        if i == len(cores):
            i = 0
        m.cor = cores[i]
        i = i + 1

    i = 0
    for n in nte:
        if i == len(cores):
            i = 0
        n.cor = cores[i]
        i = i + 1

    i = 0
    for b in bairro:
        if i == len(cores):
            i = 0
        b.cor = cores[i]
        i = i + 1

    grafico ={
        "municipios": municipio,
        "ntes": nte,
        "bairros": bairro
    }
    return render(request, "home/SEDE_grafico.html", grafico)

@login_required(login_url = "/login/")
def criar_sede(request):
    form = SedeForm(request.POST)

    if request.method == "GET":
        form = SedeForm()

        return render(request, url_criar_sede, {"form": form})
    else:
        if form.is_valid():    
            nome_sede = form.cleaned_data.get("nome_sede")
            codigo_inep_sede = form.cleaned_data.get("codigo_inep_sede")
            telefone_sede = form.cleaned_data.get("telefone_sede")
            nome_responsavel_sede = form.cleaned_data.get("nome_responsavel_sede")
            bairro_sede = form.cleaned_data.get("bairro_sede")
            email_sede = form.cleaned_data.get("email_sede")
            id_nte_sede = form.cleaned_data.get("id_nte_sede")
            id_municipio_sede = form.cleaned_data.get("id_municipio_sede")
            
            sede = Sede.objects.create(nome_sede = nome_sede,
            codigo_inep_sede = codigo_inep_sede, telefone_sede = telefone_sede,
            nome_responsavel_sede = nome_responsavel_sede, bairro_sede = bairro_sede,
            email_sede = email_sede, id_nte_sede = id_nte_sede,
            id_municipio_sede = id_municipio_sede)
                
            sede.save()
            msg = "Sede Cadastrada com Sucesso!"
            return render(request, url_dashboard_sede,cadastrado_sede(form, msg, False))
        
        return render(request, url_criar_sede,cadastrado_sede(form, form.errors, True))

@login_required(login_url = "/login/")
def consultar_sede(request):
    lista_por_sede = None
    sede = Sede.objects.all()
    
    if "buscar_sede" in request.GET:
        sede_consulta = request.GET["buscar_sede"]
        bairro_consulta = request.GET["buscar_bairro"]
        municipio_consulta = request.GET["buscar_municipio"]
        if consultar_sede:
            lista_por_sede = sede.filter(Q(nome_sede__icontains = sede_consulta))
            lista_por_bairro = lista_por_sede.filter(Q(bairro_sede__icontains = bairro_consulta))
            lista_por_municipio = lista_por_bairro.filter(Q(id_municipio_sede__nome_municipio__icontains = municipio_consulta))
    
    if lista_por_municipio:
        dados = {
            "sedes": lista_por_municipio,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "sedes": lista_por_municipio,
            "error": True,
            "mensagem": "Nenhuma Sede Localizada!"
        }

    return render(request, url_dashboard_sede, dados)
    
@login_required(login_url = "/login/")    
def editar_sede(request,id_sede):
    sede = Sede.objects.get(id_sede = id_sede)
    form = SedeForm(initial = model_to_dict(sede))

    edt_sede = { 
        "sede":sede,
        "form": form  }
    
    if request.method == "POST":
        form = SedeForm(request.POST, instance = sede)

        if form.is_valid():
            sede.save()

            msg = "Sede Alterada com Sucesso!"
            return render(request, url_dashboard_sede,cadastrado_sede(form, msg, False))

        return render(request, url_criar_sede,cadastrado_sede(form, form.errors, True))
    else:        
        return render(request, url_editar_sede, edt_sede)

def cadastrado_sede(form, msg, error):
    sede = Sede.objects.all()
    dados = {
        "sedes": sede,
        "form": form,
        "error": error,
        "mensagem":msg
    }
    return dados

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

