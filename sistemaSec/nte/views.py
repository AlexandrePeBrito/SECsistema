from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.nte.models import NTE


@login_required(login_url="/login/")
def criar_nte(request):
    if request.method == "POST":
        nome_direitor_NTE = request.POST['nome_direitor_NTE']
        email = request.POST['email']
        telefone = request.POST['telefone']

        erros =[{"Erro": 'Supervisor do NTE', "Valido": isEmpty(nome_direitor_NTE), "Mensagem": "Nome Invalido"},
                {"Erro": 'Telefone do NTE', "Valido": isEmpty(telefone), "Mensagem": "Telefone Invalido"},
                {"Erro": 'Email do NTE', "Valido": isEmpty(email), "Mensagem": "Email Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            nte = NTE.objects.create(nome_direitor_NTE = nome_direitor_NTE,
                email_NTE = email, telefone_NTE = telefone)
            
            nte.save()
            msg = 'NTE Cadastrado com Sucesso!'
        return render(request,"home/NTE_dashboard.html",cadastrado_nte(msg))
    else:
        return redirect("sistemaSec/templates/home/NTE_criar_nte.html")

@login_required(login_url="/login/")
def consultar_nte(request):
    lista_por_nte=None
    nte = NTE.objects.all()
    
    if 'buscar_nte' in request.GET:
        nte_consulta=request.GET['buscar_nte']
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
    nte = get_object_or_404(NTE, pk=id_NTE)
    edt_nte = { 'nte':nte }
    return render(request, 'home/NTE_editar_nte.html', edt_nte)

@login_required(login_url="/login/")
def atualizar_nte(request):
    if request.method == 'POST':
        id_NTE = request.POST['id_nte']
        nt = NTE.objects.get(pk=id_NTE)
        nt.nome_direitor_NTE = request.POST['nome_direitor']
        nt.email_NTE = request.POST['email']
        nt.telefone_NTE = request.POST['telefone']

        
        erros =[{"Erro": 'Supervisor do NTE', "Valido": isEmpty(nt.nome_direitor_NTE), "Mensagem": "Nome Invalido"},
                {"Erro": 'Telefone do NTE', "Valido": isEmpty(nt.telefone_NTE), "Mensagem": "Telefone Invalido"},
                {"Erro": 'Email do NTE', "Valido": isEmpty(nt.email_NTE), "Mensagem": "Email Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            nt.save()
    
            msg = 'NTE Alterado com Sucesso!'
        return render(request,"home/NTE_dashboard.html",cadastrado_nte(msg))
    else:
        return redirect("home/NTE_criar_nte.html")


def cadastrado_nte(msg):
    nte = NTE.objects.all()
    dados ={
        'NTEs': nte,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

