from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from sistemaSec.municipio.models import Municipio
from .forms import MunicipioForm
from django.forms.models import model_to_dict

url_criar_municipio = "home/MUNI_criar_municipio.html"
url_dashboard_municipio = "home/MUNI_dashboard.html"
url_editar_municipio = "home/MUNI_editar_municipio.html"

def grafico_municipio(request):
    nte = Municipio.objects.raw("Select 1 as id_municipio, id_NTE as nome, count(id_municipio) as qtd, '#ff0000' as cor from muni_municipio join nte_nte on nte_nte.id_NTE = muni_municipio.id_nte_municipio_id group by id_NTE")

    cores = ["#ed0919", "#2a07f0", "#b33062", "#5652c7", "#ed0919", "#2a07f0", "#b33062", "#5652c7"]
    #"#1de9b6", "#A389D4", "#04a9f5", 
    i = 0
    for n in nte:
        if i == len(cores):
            i = 0
        n.cor = cores[i]
        i = i + 1

    grafico ={
        "ntes": nte,
    }

    return render(request, "home/MUNI_grafico.html", grafico)
    
@login_required(login_url = "/login/")
def criar_municipio(request):
    form = MunicipioForm(request.POST)

    if request.method == "GET":
        form = MunicipioForm()

        return render(request, url_criar_municipio, {"form": form})
    else:
        if form.is_valid():
            nome_municipio = form.cleaned_data.get("nome_municipio")
            nte = form.cleaned_data.get("id_nte_municipio")
            
            municipio = Municipio.objects.create(nome_municipio = nome_municipio,
                    id_nte_municipio = nte)
                
            municipio.save()
            msg = "Municipio Cadastrado com Sucesso!"
            return render(request, url_dashboard_municipio,cadastrado_municipio(form, msg))
        
        msg = "Ocorreu um ERRO no Cadastro!"
        return render(request, url_dashboard_municipio,cadastrado_municipio(form, msg))

@login_required(login_url ="/login/")
def consultar_municipio(request):
    lista_por_municipio = None
    muncipio = Municipio.objects.all()
    
    if "buscar_municipio" in request.GET:
        municipio_consulta = request.GET["buscar_municipio"]
        nte_consulta = request.GET["buscar_nte"]
        if consultar_municipio:
            lista_por_municipio = muncipio.filter(Q(nome_municipio__icontains = municipio_consulta))
            listar_por_nte = lista_por_municipio.filter(Q(id_nte_municipio__id_NTE__icontains = nte_consulta))
    
    if listar_por_nte:
        dados = {
            "municipios": listar_por_nte,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "municipios": listar_por_nte,
            "error": True,
            "mensagem": "Nenhum Municipio Localizado!"
        }
    return render(request, url_dashboard_municipio,dados)
    
@login_required(login_url = "/login/")    
def editar_municipio(request,id_municipio):
    municipio = Municipio.objects.get(id_municipio = id_municipio)
    form = MunicipioForm(initial = model_to_dict(municipio))

    edt_municipio = { 
        "municipio":municipio,
        "form": form }

    if request.method == "POST":
        form = MunicipioForm(request.POST, instance = municipio)

        if form.is_valid():
            municipio.save()

            msg = "Municipio Alterado com Sucesso!"
            return render(request, url_dashboard_municipio,cadastrado_municipio(form, msg))

        msg = "Ocorreu um erro!"
        return render(request, url_dashboard_municipio,cadastrado_municipio(form, msg))
    else:
        return render(request, url_editar_municipio,edt_municipio)

def cadastrado_municipio(form, msg):
    municipios = Municipio.objects.all()
    dados = {
        "municipios": municipios,
        "form": form,
        "mensagem":msg
    }
    return dados

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
