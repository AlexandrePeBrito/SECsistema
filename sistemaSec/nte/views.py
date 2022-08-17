from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.nte.models import NTE
from .forms import NTEForm
from django.forms.models import model_to_dict

url_criar_nte = "home/NTE_criar_nte.html"
url_dashboard_nte = "home/NTE_dashboard.html"
url_editar_nte = "home/NTE_editar_nte.html"

@login_required(login_url="/login/")
def criar_nte(request):
    form = NTEForm(request.POST)
    print(url_criar_nte)
    if request.method == "GET":
        form = NTEForm()
        return render(request,url_criar_nte, {"form": form})

    else: 
        if form.is_valid(): 
            nome_direitor_NTE = form.cleaned_data.get("nome_direitor_NTE")
            email = form.cleaned_data.get("email_NTE")
            telefone = form.cleaned_data.get("telefone_NTE")

        
            nte = NTE.objects.create(nome_direitor_NTE = nome_direitor_NTE,
                email_NTE = email, telefone_NTE = telefone)
            
            nte.save()
            msg = "NTE Cadastrado com Sucesso!"

            return render(request, url_dashboard_nte,cadastrado_nte(form, msg, False))

        return render(request, url_criar_nte,cadastrado_nte(form, form.errors, True))
        

@login_required(login_url="/login/")
def consultar_nte(request):
    lista_por_nte=None
    nte = NTE.objects.all()
    
    if "buscar_nte" in request.GET:
        nte_consulta=request.GET["buscar_nte"]
        if consultar_nte:
            lista_por_nte= nte.filter(Q(id_NTE__icontains=nte_consulta))
    
    if lista_por_nte:
        dados = {
            "NTEs": lista_por_nte,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "NTEs": lista_por_nte,
            "error": True,
            "mensagem": "Nenhum NTE Localizado!"
        }

    return render(request, url_dashboard_nte,dados)
    
@login_required(login_url="/login/")    
def editar_nte(request,id_NTE):
    nte = NTE.objects.get(id_NTE=id_NTE)
    form = NTEForm(initial = model_to_dict(nte))

    edt_nte = { 
        "nte":nte,
        "form": form  }

    if request.method == "POST":
        form = NTEForm(request.POST, instance = nte)
        if form.is_valid():
            nte.save()

            msg = "NTE Alterado com Sucesso!"
            return render(request, url_dashboard_nte,cadastrado_nte(form, msg, False))

        return render(request, url_criar_nte,cadastrado_nte(form, form.errors, True))
    else:
        return render(request, url_editar_nte, edt_nte)


def cadastrado_nte(form, msg, error):
    nte = NTE.objects.all()
    dados ={
        "NTEs": nte,
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

