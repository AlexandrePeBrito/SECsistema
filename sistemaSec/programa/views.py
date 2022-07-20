from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.programa.models import Programa


@login_required(login_url="/login/")
def criar_programa(request):
    if request.method == "POST":
        nome_programa = request.POST['nome_programa']
        
        erros =[{"Erro": 'Nome do Programa', "Valido": isEmpty(nome_programa), "Mensagem": "Nome Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            programa = Programa.objects.create(nome_programa = nome_programa)
            
            programa.save()
            msg = 'Programa Cadastrado com Sucesso!'
        return render(request,"home/PROG_dashboard.html",cadastrado_programa(msg))
    else:
        return redirect("sistemaSec/templates/home/PROG_criar_programa.html")

@login_required(login_url="/login/")
def consultar_programa(request):
    lista_por_programa=None
    programa = Programa.objects.all()
    
    if 'buscar_programa' in request.GET:
        programa_consulta=request.GET['buscar_programa']
        if consultar_programa:
            lista_por_programa= programa.filter(Q(nome_programa__icontains=programa_consulta))
    
    dados = {"programas": lista_por_programa}
    return render(request,"home/PROG_buscar_programa.html",dados)
    
@login_required(login_url="/login/")    
def editar_programa(request,id_programa):
    programa = get_object_or_404(Programa, pk=id_programa)
    edt_programa = { 'programa':programa }
    return render(request, 'home/PROG_editar_programa.html', edt_programa)

@login_required(login_url="/login/")
def atualizar_programa(request):
    if request.method == 'POST':
        id_programa = request.POST['id_programa']
        prog = Programa.objects.get(pk=id_programa)
        prog.nome_programa = request.POST['nome_programa']

        erros =[{"Erro": 'Nome do Programa', "Valido": isEmpty(prog.nome_programa), "Mensagem": "Nome Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            prog.save()

            msg = 'Programa Alterado com Sucesso!'
        return render(request,"home/PROG_dashboard.html",cadastrado_programa(msg))
    else:
        return redirect("home/PROG_criar_programa.html")


def cadastrado_programa(msg):
    programa = Programa.objects.all()
    dados ={
        'programas': programa,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
