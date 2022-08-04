from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.nte.models import NTE
from .forms import NTEForm
from django.forms.models import model_to_dict

@login_required(login_url="/login/")
def criar_nte(request):
    form = NTEForm(request.POST)

    if request.method == "GET":
        form = NTEForm()
        return render(request,"home/NTE_criar_nte.html", {"form": form})

    else: 
        if form.is_valid(): 
            nome_direitor_NTE = form.cleaned_data.get("nome_direitor_NTE")
            email = form.cleaned_data.get("email_NTE")
            telefone = form.cleaned_data.get("telefone_NTE")

        
            nte = NTE.objects.create(nome_direitor_NTE = nome_direitor_NTE,
                email_NTE = email, telefone_NTE = telefone)
            
            nte.save()
            msg = "NTE Cadastrado com Sucesso!"

            return render(request,"home/NTE_dashboard.html",cadastrado_nte(form, msg))

        msg = "Ocorreu um ERRO no Cadastro!"
        return render(request,"home/NTE_dashboard.html",cadastrado_nte(form, msg))

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

    return render(request,"home/NTE_dashboard.html",dados)
    
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
            return render(request,"home/NTE_dashboard.html",cadastrado_nte(form, msg))

        msg = "Ocorreu um erro!"
        return render(request,"home/NTE_dashboard.html",cadastrado_nte(form, msg))
    else:
        return render(request, "home/NTE_editar_nte.html", edt_nte)


def cadastrado_nte(form, msg):
    nte = NTE.objects.all()
    dados ={
        "NTEs": nte,
        "form": form,
        "mensagem":msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

