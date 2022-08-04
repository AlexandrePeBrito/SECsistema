from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.edital.models import Edital
from .forms import EditalForm
from django.forms.models import model_to_dict

@login_required(login_url="/login/")
def criar_edital(request):
    form = EditalForm(request.POST)

    if request.method == "GET":
        form = EditalForm()

        return render(request, 'home/EDTL_criar_edital.html', {'form': form})
    else:
        if form.is_valid():
            id_edital = form.cleaned_data.get('id_edital')
            quantidade_vagas = form.cleaned_data.get('quantidade_vagas_edital')
            programa = form.cleaned_data.get('id_programa_edital')
        
            edital = Edital.objects.create(id_edital = id_edital,
                quantidade_vagas_edital = quantidade_vagas,
                id_programa_edital = programa)
            
            edital.save()
            msg = 'Edital Cadastrado com Sucesso!'
            return render(request,"home/EDTL_dashboard.html",cadastrado_edital(form, msg))

        msg = 'Ocorreu um Error!'
        return render(request,"home/EDTL_dashboard.html",cadastrado_edital(form, msg))

@login_required(login_url="/login/")
def consultar_edital(request):
    lista_por_edital=None
    edital = Edital.objects.all()
    
    if 'buscar_edital' in request.GET:
        edital_consulta=request.GET['buscar_edital']
        programa_consulta=request.GET['buscar_programa']
        if consultar_edital:
            lista_por_edital = edital.filter(Q(id_edital__icontains=edital_consulta))
            listar_por_programa = lista_por_edital.filter(Q(id_programa_edital__nome_programa__icontains=programa_consulta))
    
    if listar_por_programa:
        dados = {
            "editais": listar_por_programa,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "editais": listar_por_programa,
            "error": True,
            "mensagem": "Nenhum Edital Localizado!"
        }
    return render(request,"home/EDTL_dashboard.html",dados)
    
@login_required(login_url="/login/")    
def editar_edital(request,id_edital):
    edital = Edital.objects.get(id_edital=id_edital)
    form = EditalForm(initial = model_to_dict(edital))

    edt_edital = { 
        'edital':edital, 
        'form': form }
    
    if request.method == 'POST':
        form = EditalForm(request.POST, instance = edital)
        
        if form.is_valid():
            edital.save()

            msg = 'Edital Alterado com sucesso!'
            return render(request,"home/EDTL_dashboard.html",cadastrado_edital(form, msg))
        
        msg = 'Ocorreu um Erro'
        return render(request,"home/EDTL_dashboard.html",cadastrado_edital(form, msg))
    else:
        return render(request, 'home/EDTL_editar_edital.html', edt_edital)

def cadastrado_edital(form, msg):
    editais = Edital.objects.all()
    dados ={
        'editais': editais,
        'form': form,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
