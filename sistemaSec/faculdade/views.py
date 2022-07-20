from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.faculdade.models import Faculdade

@login_required(login_url="/login/")
def criar_faculdade(request):
    if request.method == "POST":
        nome_faculdade = request.POST['nome_faculdade']
        cnpj_faculdade = request.POST['cnpj_faculdade']
        direitor_faculdade = request.POST['direitor_faculdade']
        campus = request.POST['campus']
        telefone = request.POST['telefone']

        erros =[{"Erro": 'Nome da Faculdade', "Valido": isEmpty(nome_faculdade), "Mensagem": "Carga Horaria Invalida"},
                {"Erro": 'Cnpj da Faculdade', "Valido": isEmpty(cnpj_faculdade), "Mensagem": "Area Invalida"},
                {"Erro": 'Direitor da Faculdade', "Valido": isEmpty(direitor_faculdade), "Mensagem": "Edital Invalido"},
                {"Erro": 'Campus da Faculdade', "Valido": isEmpty(campus), "Mensagem": "Curso Invalido"},
                {"Erro": 'Telefone da Faculdade', "Valido": isEmpty(telefone), "Mensagem": "Curso Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            faculdade = Faculdade.objects.create(nome_faculdade = nome_faculdade,
            cnpj_faculdade = cnpj_faculdade, nome_direitor_faculdade = direitor_faculdade,
            telefone_faculdade = telefone, campus_faculdade = campus)
        
            faculdade.save()
            msg = 'Estagio Cadastrado com Sucesso!'
        return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(msg))
    else:
        return redirect("sistemaSec/templates/home/FACU_criar_faculdade.html")

@login_required(login_url="/login/")
def consultar_faculdade(request):
    lista_por_nome=None
    faculdade = Faculdade.objects.all()
    
    if 'buscar_faculdade' in request.GET:
        nome_consulta=request.GET['buscar_faculdade']

        if consultar_faculdade:
            lista_por_nome = faculdade.filter(Q(nome_faculdade__icontains=nome_consulta))
            
    dados = {"faculdades": lista_por_nome}
    return render(request,"home/FACU_buscar_faculdade.html",dados)
    
@login_required(login_url="/login/")    
def editar_faculdade(request,id_faculdade):
    faculdade = get_object_or_404(Faculdade, pk=id_faculdade)
    edt_faculdade = { 'faculdade':faculdade }
    return render(request, 'home/FACU_editar_faculdade.html', edt_faculdade)

@login_required(login_url="/login/")
def atualizar_faculdade(request):
    if request.method == 'POST':
        id_faculdade = request.POST['id_faculdade']
        fac = Faculdade.objects.get(pk=id_faculdade)
        fac.nome_faculdade = request.POST['nome_faculdade']
        fac.cnpj_faculdade = request.POST['cnpj_faculdade']
        fac.nome_direitor_faculdade = request.POST['nome_direitor_faculdade']
        fac.telefone_faculdade = request.POST['telefone_faculdade']
        fac.campus_faculdade = request.POST['campus_faculdade']

        erros =[{"Erro": 'Nome da Faculdade', "Valido": isEmpty(fac.nome_faculdade), "Mensagem": "Nome Invalido"},
                {"Erro": 'Cnpj da Faculdade', "Valido": isEmpty(fac.cnpj_faculdade), "Mensagem": "CNPJ Invalido"},
                {"Erro": 'Direitor da Faculdade', "Valido": isEmpty(fac.nome_direitor_faculdade), "Mensagem": "Direitor Invalido"},
                {"Erro": 'Campus da Faculdade', "Valido": isEmpty(fac.campus_faculdade), "Mensagem": "Campus Invalido"},
                {"Erro": 'Telefone da Faculdade', "Valido": isEmpty( fac.telefone_faculdade), "Mensagem": "Telefone Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            fac.save()
            msg = 'Estagio Alterado com Sucesso!'
        return render(request,"home/FACU_dashboard.html",cadastrado_faculdade(msg))
    else:
        return redirect("home/FACU_criar_faculdade.html")


def cadastrado_faculdade(msg):
    faculdades = Faculdade.objects.all()
    dados ={
        'faculdades': faculdades,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

