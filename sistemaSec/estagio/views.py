from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.estagio.models import Estagio
from sistemaSec.edital.models import Edital
from sistemaSec.curso.models import Curso

@login_required(login_url="/login/")
def criar_estagio(request):
    if request.method == "POST":
        carga_horaria_estagio = request.POST['carga_horaria_estagio']
        area_estagio = request.POST['area_estagio']
        id_edital_estagio = request.POST['id_edital_estagio']
        id_cursos_estagio = request.POST['id_cursos_estagio']

        erros =[{"Erro": 'Carga Horaria do Estagio', "Valido": isEmpty(carga_horaria_estagio), "Mensagem": "Carga Horaria Invalida"},
                {"Erro": 'Area do Estagio', "Valido": isEmpty(area_estagio), "Mensagem": "Area Invalida"},
                {"Erro": 'Edital do Estagio', "Valido": isEmpty(id_edital_estagio), "Mensagem": "Edital Invalido"},
                {"Erro": 'Curso do Estagio', "Valido": isEmpty(id_cursos_estagio), "Mensagem": "Curso Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            curso = Curso.objects.get(id_curso=id_cursos_estagio)
            edital = Edital.objects.get(id_edital=id_edital_estagio)
            estagio = Estagio.objects.create(carga_horaria_estagio = carga_horaria_estagio,
            area_estagio = area_estagio, id_edital_estagio = edital, id_cursos_estagio = curso)
        
            estagio.save()
            msg = 'Estagio Cadastrado com Sucesso!'
        return render(request,"home/ESTG_dashboard.html",cadastrado_estagio(msg))
    else:
        return redirect("sistemaSec/templates/home/ESTG_criar_estagio.html")

@login_required(login_url="/login/")
def consultar_estagio(request):
    lista_por_area = None
    listar_por_edital = None
    listar_por_curso = None
    estagios = Estagio.objects.all()
    
    if 'buscar_area' in request.GET:
        area_consulta = request.GET['buscar_area']
        edital_consulta = request.GET['buscar_edital']
        curso_consulta = request.GET['buscar_curso']

        if consultar_estagio:
            lista_por_area = estagios.filter(Q(area_estagio__icontains=area_consulta))
            listar_por_edital = lista_por_area.filter(Q(id_edital_estagio__id_edital__icontains=edital_consulta))
            listar_por_curso = listar_por_edital.filter(Q(id_cursos_estagio__nome_curso__icontains=curso_consulta))
    
    if listar_por_curso:
        dados = {
            "estagios": listar_por_curso,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "estagios": listar_por_curso,
            "error": True,
            "mensagem": "Nenhum Estagio Localizado!"
        }
    return render(request,"home/ESTG_dashboard.html",dados)
    
@login_required(login_url="/login/")    
def editar_estagio(request,id_estagio):
    estagio = get_object_or_404(Estagio, pk=id_estagio)

    editar_estagio = { 'estagio':estagio }
    return render(request, 'home/ESTG_editar_estagio.html', editar_estagio)

@login_required(login_url="/login/")
def atualizar_estagio(request):
    if request.method == 'POST':
        id_estagio = request.POST['id_estagio']
        estg = Estagio.objects.get(pk=id_estagio)
        estg.carga_horaria_estagio = request.POST['carga_horaria_estagio']
        estg.area_estagio = request.POST['area_estagio']
        curso_estagio = request.POST['id_cursos_estagio']
        edital_estagio = request.POST['id_edital_estagio']
        
        erros =[{"Erro": 'Carga Horaria do Estagio', "Valido": isEmpty(estg.carga_horaria_estagio), "Mensagem": "Carga Horaria Invalida"},
                {"Erro": 'Area do Estagio', "Valido": isEmpty(estg.area_estagio), "Mensagem": "Area Invalida"},
                {"Erro": 'Edital do Estagio', "Valido": isEmpty(edital_estagio), "Mensagem": "Edital Invalido"},
                {"Erro": 'Curso do Estagio', "Valido": isEmpty(curso_estagio), "Mensagem": "Curso Invalido"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:        
            edital = Edital.objects.get(id_edital = edital_estagio)
            estg.id_edital_estagio = edital
            curso = Curso.objects.get(id_curso = curso_estagio)
            estg.id_cursos_estagio = curso
            estg.save()

            msg = 'Estagio Alterado com Sucesso!'
        return render(request,"home/ESTG_dashboard.html",cadastrado_estagio(msg))
    else:
        return redirect("home/ESTG_criar_estagio.html")



def cadastrado_estagio(msg):
    estagios = Estagio.objects.all()
    dados ={
        'estagios': estagios,
        'mensagem':msg
    }
    return dados

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

