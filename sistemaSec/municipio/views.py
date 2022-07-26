from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from sistemaSec.municipio.models import Municipio
from sistemaSec.nte.models import NTE

@login_required(login_url="/login/")
def criar_municipio(request):
    if request.method == "POST":
        nome_municipio = request.POST['nome_municipio']
        id_nte_municipio = request.POST['id_nte_municipio']
        
        erros =[{"Erro": 'Nome do Municipio', "Valido": isEmpty(nome_municipio), "Mensagem": "Nome Invalido"},
                {"Erro": 'Nte do Municipio', "Valido": isEmpty(id_nte_municipio), "Mensagem": "NTE Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            nte = NTE.objects.get(id_NTE=id_nte_municipio)
            municipio = Municipio.objects.create(nome_municipio = nome_municipio,
                id_nte_municipio = nte)
            
            municipio.save()
            msg = 'Municipio Cadastrado com Sucesso!'
        return render(request,"home/MUNI_dashboard.html",cadastrado_municipio(msg))
    else:
        return redirect("sistemaSec/templates/home/MUNI_criar_municipio.html")

@login_required(login_url="/login/")
def consultar_municipio(request):
    lista_por_municipio=None
    muncipio = Municipio.objects.all()
    
    if 'buscar_municipio' in request.GET:
        municipio_consulta=request.GET['buscar_municipio']
        nte_consulta=request.GET['buscar_nte']
        if consultar_municipio:
            lista_por_municipio = muncipio.filter(Q(nome_municipio__icontains = municipio_consulta))
            listar_por_nte = lista_por_municipio.filter(Q(id_nte_municipio__id_NTE__icontains = nte_consulta))
    
    if listar_por_nte:
        dados = {
            "municipios": listar_por_nte,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "municipios": listar_por_nte,
            "error": True,
            "mensagem": "Nenhum Municipio Localizado!"
        }
    return render(request,"home/MUNI_dashboard.html",dados)
    
@login_required(login_url="/login/")    
def editar_municipio(request,id_municipio):
    municipio = get_object_or_404(Municipio, pk=id_municipio)
    edt_municipio = { 'municipio':municipio }
    return render(request, 'home/MUNI_editar_municipio.html', edt_municipio)

@login_required(login_url="/login/")
def atualizar_municipio(request):
    if request.method == 'POST':
        cod_municipio = request.POST['id_municipio']
        munp = Municipio.objects.get(pk=cod_municipio)
        munp.id_municipio= cod_municipio
        munp.nome_municipio = request.POST['nome_municipio']
        nte = request.POST['id_nte_municipio']

        erros =[{"Erro": 'Nome do Municipio', "Valido": isEmpty(munp.nome_municipio), "Mensagem": "Nome Invalido"},
                {"Erro": 'Nte do Municipio', "Valido": isEmpty(nte), "Mensagem": "NTE Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            Nte = NTE.objects.get(id_NTE=nte)
            munp.id_nte_municipio = Nte
            munp.save()

            msg = 'Municipio Cadastrado com Sucesso!'
        return render(request,"home/MUNI_dashboard.html",cadastrado_municipio(msg))

    else:
        return redirect("home/MUNI_criar_municipio.html")


def cadastrado_municipio(msg):
    municipios = Municipio.objects.all()
    dados ={
        'municipios': municipios,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True
