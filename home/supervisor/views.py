from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from home.supervisor.models import Supervisor
from django.db.models import Q
from .forms import SupervisorForm
from django.forms.models import model_to_dict

url_criar_supervisor = "home/SUPE_criar_supervisor.html"
url_dashboard_supervisor = "home/SUPE_dashboard.html"
url_editar_supervisor = "home/SUPE_editar_supervisor.html"

# Views

def grafico_supervisor(request):
    sede = Supervisor.objects.raw("Select 1 as id_supervisor, nome_sede as nome, count(id_supervisor) as qtd, '#ff0000' as cor from supervisor_supervisor join SEDE_sede on sede_supervisor_id=id_sede group by nome_sede")
    
    cores = ["#ed0919", "#2a07f0", "#b33062", "#5652c7", "#ed0919", "#2a07f0", "#b33062", "#5652c7"]
    i = 0
    for s in sede:
        s.cor = cores[i]
        i += 1

    grafico = {"sedes": sede}
    return render(request, "home/SUPE_grafico.html", grafico) 

@login_required(login_url="/login/")
def criar_supervisor(request):
    form = SupervisorForm(request.POST or None)
    
    if request.method == "GET":
        return render(request, url_criar_supervisor, {"form": form})
    
    if form.is_valid():
        nome_supervisor = form.cleaned_data.get("nome_supervisor")
        email_supervisor = form.cleaned_data.get("email_supervisor")
        telefone_supervisor = form.cleaned_data.get("telefone_supervisor")
        sede_supervisor = form.cleaned_data.get("sede_supervisor")
        
        supervisor = Supervisor.objects.create(nome_supervisor=nome_supervisor,
            email_supervisor=email_supervisor, telefone_supervisor=telefone_supervisor, sede_supervisor=sede_supervisor)
        
        supervisor.save()
        msg = "Supervisor Cadastrado com Sucesso!"
        return render(request, url_dashboard_supervisor, cadastrado_supervisor(SupervisorForm(), msg, False))
    
    return render(request, url_criar_supervisor, cadastrado_supervisor(form, "Ocorreu um ERRO no Cadastro!", True))


@login_required(login_url="/login/")
def consultar_supervisor(request):
    lista_por_nome = None
    supervisores = Supervisor.objects.all()
    
    if "buscar_supervisor" in request.GET:
        nome_consulta = request.GET["buscar_supervisor"]

        if nome_consulta:
            lista_por_nome = supervisores.filter(Q(nome_supervisor__icontains=nome_consulta))
    
    dados = {
        "supervisores": lista_por_nome,
        "error": not bool(lista_por_nome),
        "mensagem": "Consulta Feita com Sucesso!" if lista_por_nome else "Nenhum Supervisor Localizado!"
    }
    return render(request, url_dashboard_supervisor, dados)
    
@login_required(login_url="/login/")    
def editar_supervisor(request, id_supervisor):
    supervisor = Supervisor.objects.get(id_supervisor=id_supervisor)
    
    form = SupervisorForm(initial=model_to_dict(supervisor))
    editar_supervisor = {"supervisor": supervisor, "form": form}

    if request.method == "POST":
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            supervisor.save()
            msg = "Supervisor Alterado com Sucesso!"
            return render(request, url_dashboard_supervisor, cadastrado_supervisor(form, msg, False))
        return render(request, url_criar_supervisor, cadastrado_supervisor(form, form.errors, True))
    
    return render(request, url_editar_supervisor, editar_supervisor)
    

def cadastrado_supervisor(form, msg, error):
    supervisores = Supervisor.objects.all()
    dados = {
        "supervisores": supervisores,
        "form": form,
        "error": error,
        "mensagem": msg
    }
    return dados
