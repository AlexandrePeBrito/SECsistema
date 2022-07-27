from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.sede.models import Sede

@login_required(login_url="/login/")
def criar_supervisor(request):
    if request.method == "POST":
        nome_supervisor = request.POST['nome_supervisor']
        email = request.POST['email']
        telefone = request.POST['telefone']
        sede_supervisor = request.POST['sede_supervisor']

        erros =[{"Erro": 'Nome', "Valido": isEmpty(nome_supervisor), "Mensagem": "Nome Invalido"},
                {"Erro": 'Email', "Valido": isEmpty(email), "Mensagem": "Email Invalido"},
                {"Erro": 'Telefone', "Valido": isEmpty(telefone), "Mensagem": "Telefone Invalido"},
                {"Erro": 'Supervisor', "Valido": isEmpty(sede_supervisor), "Mensagem": "Sede Invalida"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")

            return render(request,"home/SUPE_criar_supervisor.html")

        else:
            sede = Sede.objects.get(id_sede = sede_supervisor)
            supervisor = Supervisor.objects.create(nome_supervisor = nome_supervisor,
                email_supervisor = email, telefone_supervisor = telefone)
            
            supervisor.sede_supervisor.add(sede)
            supervisor.save()

            msg = 'Supervisor Cadastrado com Sucesso!'
            return render(request, 'home/SUPE_dashboard.html',cadastrado_supervisor(msg))

    else:
        sedes = Sede.objects.all()
        print(sedes)
        return render(request, "home/SUPE_criar_supervisor.html", {"sedes":sedes})

@login_required(login_url="/login/")
def consultar_supervisor(request):
    lista_por_nome = None
    supervisores = Supervisor.objects.all()
    
    if 'buscar_supervisor' in request.GET:
        nome_consulta=request.GET['buscar_supervisor']

        if consultar_supervisor:
            lista_por_nome = supervisores.filter(Q(nome_supervisor__icontains=nome_consulta))
    
    if lista_por_nome:
        dados = {
            "supervisores": lista_por_nome,
            "error": False,
            "mensagem": "Consulta Feita com Sucesso!"
        }
    else:
        dados = {
            "supervisores": lista_por_nome,
            "error": True,
            "mensagem": "Nenhum Supervisor Localizado!"
        }
   
    return render(request,"home/SUPE_dashboard.html",dados)
    
@login_required(login_url="/login/")    
def editar_supervisor(request,id_supervisor):
    supervisor = get_object_or_404(Supervisor, pk=id_supervisor)
    sede = supervisor.sede_supervisor.all()

    editar_supervisor = { 'supervisor':supervisor,
                          'sede': sede }
    return render(request, 'home/SUPE_editar_supervisor.html', editar_supervisor)

@login_required(login_url="/login/")
def atualizar_supervisor(request):
    if request.method == 'POST':
        id_supervisor = request.POST['id_supervisor']
        sup = Supervisor.objects.get(pk=id_supervisor)
        sup.nome_supervisor = request.POST['nome_supervisor']
        sup.email_supervisor = request.POST['email']
        sup.telefone_supervisor = request.POST['telefone']
        sede_supervisor = request.POST['sede_supervisor']

        erros =[{"Erro": 'Nome do Supervisor', "Valido": isEmpty(sup.nome_supervisor), "Mensagem": "Nome Invalido"},
                {"Erro": 'Email do Supervisor', "Valido": isEmpty(sup.email_supervisor), "Mensagem": "Email Invalido"},
                {"Erro": 'Telefone do Supervisor', "Valido": isEmpty(sup.telefone_supervisor), "Mensagem": "Telefone Invalido"},
                {"Erro": 'Sede do Supervisor ', "Valido": isEmpty(sede_supervisor), "Mensagem": "Sede Invalida"}]
        
        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)

        if len(list(ExisteErros))>0:
            print("Existe erros")
        else:
            sede = Sede.objects.get(id_sede = sede_supervisor)
            sup.sede_supervisor.add(sede)
            sup.save()

            msg = 'Supervisor Alterado com Sucesso!'
        return render(request,"home/SUPE_dashboard.html",cadastrado_supervisor(msg))
    else:
        return redirect("home/SUPE_criar_supervisor.html")


def cadastrado_supervisor(msg):
    supervisor = Supervisor.objects.all()
    dados ={
        'supervisores': supervisor,
        'mensagem':msg
    }
    return dados


def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True


