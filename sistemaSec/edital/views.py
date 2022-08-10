from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from sistemaSec.edital.models import Edital
from .forms import EditalForm
from django.forms.models import model_to_dict

url_criar_edital = "home/EDTL_criar_edital.html"
url_dashboard_edital = "home/EDTL_dashboard.html"
url_editar_edital = "home/EDTL_editar_edital.html"

@login_required(login_url = "/login/")
def criar_edital(request):
    form = EditalForm(request.POST)

    if request.method == "GET":
        form = EditalForm()

        return render(request, url_criar_edital, {"form": form})
    else:
        if form.is_valid():
            id_edital = form.cleaned_data.get("id_edital")
            quantidade_vagas = form.cleaned_data.get("quantidade_vagas_edital")
            
        
            edital = Edital.objects.create(id_edital = id_edital,
                quantidade_vagas_edital = quantidade_vagas)
            
            edital.save()
            msg = "Edital Cadastrado com Sucesso!"
            return render(request, url_dashboard_edital, cadastrado_edital(form, msg))

        msg = "Ocorreu um Error!"
        return render(request, url_dashboard_edital, cadastrado_edital(form, msg))

@login_required(login_url = "/login/")
def consultar_edital(request):
    lista_por_edital = None
    edital = Edital.objects.all()
    
    if "buscar_edital" in request.GET:
        edital_consulta=request.GET["buscar_edital"]
        if consultar_edital:
            lista_por_edital = edital.filter(Q(id_edital__icontains = edital_consulta))
    
    if lista_por_edital:
        dados = {
            "editais": lista_por_edital,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "editais": lista_por_edital,
            "error": True,
            "mensagem": "Nenhum Edital Localizado!"
        }
    return render(request, url_dashboard_edital, dados)
    
@login_required(login_url = "/login/")    
def editar_edital(request,id_edital):
    edital = Edital.objects.get(id_edital = id_edital)
    form = EditalForm(initial = model_to_dict(edital))

    edt_edital = { 
        "edital":edital, 
        "form": form }
    
    if request.method == "POST":
        form = EditalForm(request.POST, instance = edital)
        
        if form.is_valid():
            edital.save()

            msg = "Edital Alterado com sucesso!"
            return render(request, url_dashboard_edital, cadastrado_edital(form, msg))
        
        msg = "Ocorreu um Erro"
        return render(request, url_dashboard_edital, cadastrado_edital(form, msg))
    else:
        return render(request, url_editar_edital, edt_edital)

def cadastrado_edital(form, msg):
    editais = Edital.objects.all()
    dados = {
        "editais": editais,
        "form": form,
        "mensagem":msg
    }
    return dados

def is_empty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
