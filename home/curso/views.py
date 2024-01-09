from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CursoForm
from .models import Curso

@login_required(login_url="/login/")
def criar_curso(request):
    form = CursoForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Curso Cadastrado com Sucesso!"
            return render(request, "home/CUSO_dashboard.html", {"form": form, "mensagem": msg})

        msg = "Ocorreu um ERRO no Cadastro!"
        return render(request, "home/CUSO_dashboard.html", {"form": form, "mensagem": msg})

    return render(request, "home/CUSO_criar_curso.html", {"form": form})

@login_required(login_url="/login/")
def consultar_curso(request):
    lista_por_curso = None
    cursos = Curso.objects.all()

    if "buscar_curso" in request.GET:
        curso_consulta = request.GET["buscar_curso"]
        if curso_consulta:
            lista_por_curso = cursos.filter(nome_curso__icontains=curso_consulta)

    if lista_por_curso:
        return render(request, "home/CUSO_dashboard.html", {"cursos": lista_por_curso, "error": False, "mensagem": "Consulta Feita com Sucesso!"})
    else:
        return render(request, "home/CUSO_dashboard.html", {"cursos": lista_por_curso, "error": True, "mensagem": "Nenhum Curso Localizado!"})

@login_required(login_url="/login/")
def editar_curso(request, id_curso):
    curso = Curso.objects.get(id_curso=id_curso)
    form = CursoForm(request.POST or None, instance=curso)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Curso Alterado com Sucesso!"
            return render(request, "home/CUSO_dashboard.html", {"form": form, "mensagem": msg})

        msg = "Ocorreu um erro!"
        return render(request, "home/CUSO_dashboard.html", {"form": form, "mensagem": msg})
    else:
        return render(request, "home/CUSO_editar_curso.html", {"curso": curso, "form": form})
