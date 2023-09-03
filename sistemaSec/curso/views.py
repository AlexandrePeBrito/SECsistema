from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.curso.models import Curso
from .forms import CursoForm

url_criar_curso = "home/CUSO_criar_curso.html"
url_dashboard_curso = "home/CUSO_dashboard.html"
url_editar_curso = "home/CUSO_editar_curso.html"

@login_required(login_url = "/login/")
def criar_curso(request):
    form = CursoForm(request.POST)

    if request.method == "GET":
        form = CursoForm()

        return render(request, url_criar_curso, {"form": form})
    
    else:
        if form.is_valid():
            nome_curso = form.cleaned_data.get("nome_curso")
        
            curso = Curso.objects.create(nome_curso = nome_curso)
        
            curso.save()

            msg = "Curso Cadastrado com Sucesso!"
            return render(request, url_dashboard_curso, cadastrado_curso(form, msg))

        msg = "Ocorreu um ERRO no Cadastro!"
        return render(request, url_dashboard_curso, cadastrado_curso(form, msg))

@login_required(login_url = "/login/")
def consultar_curso(request):
    lista_por_curso = None
    curso = Curso.objects.all()
    
    if "buscar_curso" in request.GET:
        curso_consulta = request.GET["buscar_curso"]
        if consultar_curso:
            lista_por_curso= curso.filter(Q(nome_curso__icontains = curso_consulta))
    
    if lista_por_curso:
        dados = {
            "cursos": lista_por_curso,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "cursos": lista_por_curso,
            "error": True,
            "mensagem": "Nenhum Curso Localizado!"
        }
    return render(request, url_dashboard_curso, dados)
    
@login_required(login_url = "/login/")    
def editar_curso(request,id_curso):
    curso = Curso.objects.get(id_curso = id_curso)
    form = CursoForm(instance = curso)

    edt_curso = { 
        "curso":curso, 
        "form": form }

    if request.method == "POST":
        form = CursoForm(request.POST, instance = curso)

        if form.is_valid():
            curso.save()

            msg = "Curso Alterado com Sucesso!"
            return render(request, url_dashboard_curso, cadastrado_curso(form, msg))

        msg = "Ocorreu um erro!"
        return render(request, url_dashboard_curso, cadastrado_curso(form, msg))
    else:
        return render(request, url_editar_curso, edt_curso)

def cadastrado_curso(form, msg):
    curso = Curso.objects.all()
    dados = {
        "cursos": curso,
        "form": form,
        "mensagem":msg
    }
    return dados

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
