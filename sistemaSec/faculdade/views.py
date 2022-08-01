from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.faculdade.models import Faculdade
from .forms import FaculdadeForm

@login_required(login_url="/login/")
def criar_faculdade(request):
    form = FaculdadeForm(request.POST)

    if request.method == "GET":
        form = FaculdadeForm()

        return render(request, "home/FACU_criar_faculdade.html", {"form": form})
        
    else:
        if form.is_valid():
            nome_faculdade = form.cleaned_data.get('nome_faculdade')
            cnpj_faculdade = form.cleaned_data.get('cnpj_faculdade')
            direitor_faculdade = form.cleaned_data.get('nome_direitor_faculdade')
            campus = form.cleaned_data.get('campus_faculdade')
            telefone = form.cleaned_data.get('telefone_faculdade')

        
            faculdade = Faculdade.objects.create(nome_faculdade = nome_faculdade,
            cnpj_faculdade = cnpj_faculdade, nome_direitor_faculdade = direitor_faculdade,
            telefone_faculdade = telefone, campus_faculdade = campus)
        
            faculdade.save()
            msg = 'Faculdade Cadastrada com Sucesso!'
            return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(form, msg))
        
        msg = 'Ocorreu um ERRO no Cadastro!'
        return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(form, msg))

@login_required(login_url="/login/")
def consultar_faculdade(request):
    lista_por_nome=None
    faculdade = Faculdade.objects.all()
    
    if 'buscar_faculdade' in request.GET:
        nome_consulta=request.GET['buscar_faculdade']

        if consultar_faculdade:
            lista_por_nome = faculdade.filter(Q(nome_faculdade__icontains=nome_consulta))
            
    if lista_por_nome:
        dados = {
            "faculdades": lista_por_nome,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "faculdades": lista_por_nome,
            "error": True,
            "mensagem": "Nenhuma Faculdade Localizada!"
        }
    return render(request,"home/FACU_dashboard.html",dados)
    
@login_required(login_url="/login/")    
def editar_faculdade(request,id_faculdade):
    faculdade = Faculdade.objects.get(id_faculdade=id_faculdade)
    form = FaculdadeForm(instance = faculdade)

    edt_faculdade = { 
        'faculdade':faculdade, 
        'form': form }
    
    if request.method == 'POST':
        form = FaculdadeForm(request.POST, instance = faculdade)

        if form.is_valid():
            faculdade.save()

            msg = 'Faculdade Alterado com Sucesso!'
            return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(form, msg))

        msg = "Ocorreu um erro!"
        return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(form, msg))
    else:
        return render(request,"home/FACU_editar_faculdade.html", edt_faculdade)

def cadastrado_faculdade(form, msg):
    faculdades = Faculdade.objects.all()
    dados ={
        'faculdades': faculdades,
        'form': form,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

