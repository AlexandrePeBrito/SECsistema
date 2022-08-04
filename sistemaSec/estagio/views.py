from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.estagio.models import Estagio
from .forms import EstagioForm
from django.forms.models import model_to_dict

@login_required(login_url = "/login/")
def criar_estagio(request):
    form = EstagioForm(request.POST)

    if request.method == "GET":
        form = EstagioForm()

        return render(request, "home/ESTG_criar_estagio.html", {"form": form})
    else:
        if form.is_valid():
            carga_horaria_estagio = form.cleaned_data.get("carga_horaria_estagio")
            area_estagio = form.cleaned_data.get("area_estagio")
            id_edital_estagio = form.cleaned_data.get("id_edital_estagio")
            id_cursos_estagio = form.cleaned_data.get("id_cursos_estagio")

            estagio = Estagio.objects.create(carga_horaria_estagio = carga_horaria_estagio,
            area_estagio = area_estagio, id_edital_estagio = id_edital_estagio, id_cursos_estagio = id_cursos_estagio)
        
            estagio.save()
            msg = "Estagio Cadastrado com Sucesso!"
            return render(request,"home/ESTG_dashboard.html",cadastrado_estagio(form, msg))
        
        msg = "Ocorreu um Error!"
        return render(request,"home/ESTG_dashboard.html",cadastrado_estagio(form, msg))

@login_required(login_url = "/login/")
def consultar_estagio(request):
    lista_por_area = None
    listar_por_edital = None
    listar_por_curso = None
    estagios = Estagio.objects.all()
    
    if "buscar_area" in request.GET:
        area_consulta = request.GET["buscar_area"]
        edital_consulta = request.GET["buscar_edital"]
        curso_consulta = request.GET["buscar_curso"]

        if consultar_estagio:
            lista_por_area = estagios.filter(Q(area_estagio__icontains = area_consulta))
            listar_por_edital = lista_por_area.filter(Q(id_edital_estagio__id_edital__icontains = edital_consulta))
            listar_por_curso = listar_por_edital.filter(Q(id_cursos_estagio__nome_curso__icontains = curso_consulta))
    
    if listar_por_curso:
        dados = {
            "estagios": listar_por_curso,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "estagios": listar_por_curso,
            "error": True,
            "mensagem": "Nenhum Estagio Localizado!"
        }
    return render(request,"home/ESTG_dashboard.html",dados)
    
@login_required(login_url = "/login/")    
def editar_estagio(request,id_estagio):
    estagio = Estagio.objects.get(id_estagio = id_estagio)
    form = EstagioForm(initial = model_to_dict(estagio))

    editar_estagio = { 
        "estagio":estagio,
        "form": form }

    if request.method == "POST":
        form = EstagioForm(request.POST, instance = estagio)

        if form.is_valid():
            estagio.save()

            msg = "Estagio Alterado com sucesso!"
            return render(request, "home/ESTG_dashboard.html", cadastrado_estagio(form, msg))
        
        msg = "Ocorreu um Erro"
        return render(request, "home/ESTG_dashboard.html", cadastrado_estagio(form, msg))
    else:
        return render(request, "home/ESTG_editar_estagio.html", editar_estagio)


def cadastrado_estagio(form, msg):
    estagios = Estagio.objects.all()
    dados = {
        "estagios": estagios,
        "form": form,
        "mensagem":msg
    }

    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

