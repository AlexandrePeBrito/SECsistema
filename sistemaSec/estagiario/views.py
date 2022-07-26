# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
import re
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re
from sistemaSec.edital.models import Edital
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.programa.models import Programa
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.sede.models import Sede
from sistemaSec.estagio.models import Estagio
from sistemaSec.faculdade.models import Faculdade

@login_required(login_url="/login/")
def criar_estagiario_partiu_estagio(request):
    if request.method == "POST":
        nome_estagiario = request.POST['nome_estagiario']
        cpf = request.POST['cpf']
        rg = request.POST['rg']
        turno = request.POST['turno']
        email = request.POST['email']
        semestre = request.POST['semestre']
        nis = request.POST['nis']
        telefone = request.POST['telefone']
        responsavel = request.POST['responsavel']
        nascimento = request.POST['nascimento']
        genero = request.POST['genero']
        raca = request.POST['raca']
        bairro = request.POST['bairro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        Matricula = request.POST['Matricula']
        situaçao = request.POST['situaçao']
        supervisor = request.POST['supervisor']
        sede = request.POST['sede']
        faculdade = request.POST['faculdade']
        estagio = request.POST['estagio']

        #validacao de error
        erros = [{"Erro": 'CPF', "Valido": True, "Mensagem": "CPF Invalido"},
                 {"Erro": 'Rg', "Valido": True, "Mensagem": "Preencher RG"},
                 {"Erro": 'Nome', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Turno', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Email', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Telefone', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Semestre', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Nascimento', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Genero', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Raca', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Situacao', "Valido": True, "Mensagem": "Preencher Nome"}]

        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)
        if len(list(ExisteErros))>0:
            print("existe erros")
        else:
            sedeObj = Sede.objects.get(id_sede=sede)
            faculdadeObj = Faculdade.objects.get(id_faculdade=faculdade)
            estagioObj = Estagio.objects.get(id_estagio=estagio)
            supervisorObj = Supervisor.objects.get(id_supervisor = supervisor)
            estagiario = Estagiario.objects.create(cpf_estagiario = cpf,
                nome_estagiario = nome_estagiario, rg_estagiario = rg,
                turno_estagiario = turno, email_estagiario = email,
                semestre_estagiario = semestre, nis_pis_estagiario = nis,
                telefone_estagiario = telefone, nome_responsavel_estagiario = responsavel,
                data_nascimento_estagiario = nascimento,
                genero_estagiario = genero, raca_estagiario = raca,
                bairro_estagiario = bairro, numero_estagiario = numero,
                complemento_estagiario = complemento, matricula_estagiario = Matricula,
                situacao_estagiario = situaçao, supervisor_estagiario = supervisorObj,
                sede_estagiario = sedeObj, faculdade_estagiario = faculdadeObj,
                estagio_estagiario = estagioObj)
            
            estagiario.save()
            msg = 'Estagiario Cadastrado com Sucesso!'
        return render(request,"home/PAES_dashboard.html",cadastrado_estagiario_partiu_estagio(msg))
    else:
        return redirect("sistemaSec/templates/home/PAES_criar_estagiario.html")

@login_required(login_url="/login/")
def consultar_estagiario_partiu_estagio(request):
    
    estagiarios = Estagiario.objects.all()
    
        
    if 'buscar_estagiario_partiu_estagio' in request.GET:
        nome_consulta=request.GET['buscar_estagiario_partiu_estagio']
        cpf_consulta=request.GET['buscar_cpf_estagiario_partiu_estagio']
        situacao_consulta=request.GET['buscar_situacao_estagiario_partiu_estagio']
        turno_consulta=request.GET['buscar_turno_estagiario_partiu_estagio']
        bairro_consulta=request.GET['buscar_bairro_estagiario_partiu_estagio']
        supervisor_consulta=request.GET['buscar_supervisor_estagiario_partiu_estagio']
        sede_consulta=request.GET['buscar_sede_estagiario_partiu_estagio']
        faculdade_consulta=request.GET['buscar_faculdade_estagiario_partiu_estagio']

        if consultar_estagiario_partiu_estagio:
            lista_por_nome = estagiarios.filter(Q(nome_estagiario__icontains=nome_consulta))
            lista_por_cpf = lista_por_nome.filter(Q(cpf_estagiario__icontains=cpf_consulta))
            lista_por_situacao = lista_por_cpf.filter(Q(situacao_estagiario__icontains=situacao_consulta))
            lista_por_turno = lista_por_situacao.filter(Q(turno_estagiario__icontains=turno_consulta))
            lista_por_bairro = lista_por_turno.filter(Q(bairro_estagiario__icontains=bairro_consulta))
            lista_por_supervisor = lista_por_bairro.filter(Q(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta))
            lista_por_sede = lista_por_supervisor.filter(Q(sede_estagiario__nome_sede__icontains=sede_consulta))
            lista_por_faculdade = lista_por_sede.filter(Q(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta))

    dados = {
        "estagiarios": lista_por_faculdade
    }

    return render(request,"home/PAES_buscar_estagiario.html",dados)
    
@login_required(login_url="/login/")    
def editar_estagiario_partiu_estagio(request,cpf_estagiario):
    print(cpf_estagiario)
    estagiario = get_object_or_404(Estagiario, pk=cpf_estagiario)

    editar_estagiario_partiu_estagio = { 'estagiario':estagiario }

    return render(request, 'home/PAES_editar_estagiario.html', editar_estagiario_partiu_estagio)

@login_required(login_url="/login/")
def atualizar_estagiario_partiu_estagio(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        est = Estagiario.objects.get(pk=cpf)
        est.nome_estagiario = request.POST['nome_estagiario']
        est.cpf_estagiario = cpf
        est.rg_estagiario = request.POST['rg']
        est.turno_estagiario = request.POST['turno']
        est.email_estagiario = request.POST['email']
        est.semestre_estagiario = request.POST['semestre']
        est.nis_pis_estagiario = request.POST['nis']
        est.telefone_estagiario = request.POST['telefone']
        est.nome_responsavel_estagiario = request.POST['responsavel']
        est.data_nascimento_estagiario = request.POST['nascimento']
        est.genero_estagiario = request.POST['genero']
        est.raca_estagiario = request.POST['raca']
        est.bairro_estagiario = request.POST['bairro']
        est.numero_estagiario = request.POST['numero']
        est.complemento_estagiario = request.POST['complemento']
        est.matricula_estagiario = request.POST['Matricula']
        est.situacao_estagiario = request.POST['situaçao']
        supervisor = request.POST['supervisor']
        sede = request.POST['sede']
        faculdade = request.POST['faculdade']
        estagio = request.POST['Estagio']
        erros = [{"Erro": 'CPF', "Valido": True, "Mensagem": "CPF Invalido"},
                 {"Erro": 'Rg', "Valido": True, "Mensagem": "Preencher RG"},
                 {"Erro": 'Nome', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Turno', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Email', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Telefone', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Semestre', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Nascimento', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Genero', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Raca', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Situacao', "Valido": True, "Mensagem": "Preencher Nome"}]

        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)
        if len(list(ExisteErros))>0:
            print("existe erros")
        else:
            supervisorObj = Supervisor.objects.get(id_supervisor=supervisor)
            sedeObj = Sede.objects.get(id_sede=sede)
            faculdadeObj = Faculdade.objects.get(id_faculdade=faculdade)
            estagioObj = Estagio.objects.get(id_estagio=estagio)
            est.supervisor_estagiario = supervisorObj
            est.sede_estagiario = sedeObj
            est.faculdade_estagiario = faculdadeObj
            est.estagio_estagiario = estagioObj
            est.save()
            print(estagio)
            msg = 'Estagiario Atualizado com Sucesso!'
        return render(request,"home/PAES_dashboard.html",cadastrado_estagiario_partiu_estagio(msg))
    else:
        return redirect("home/PAES_criar_estagiario.html")









def isCpfValid(cpf):
     # Check if type is str
    if not isinstance(cpf,str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cpf)
    
    # Verify if CPF number is equal
    if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
        return False

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False

def isEmpty(campo):
    if len(campo) == 0:
        return False
    else:
        return True

def isChoiceEmpty(campo):
    if campo == 0:
        return False
    else:
        return True

def cadastrado_estagiario_partiu_estagio(msg):
    programa_consulta = get_object_or_404(Programa,id_programa=1)
    sede_consulta = Edital.objects.filter(id_programa_edital_id=programa_consulta)
    estagio = Estagio.objects.filter(id_edital_estagio_id__in=sede_consulta)
    estagiario = Estagiario.objects.filter(estagio_estagiario_id__in=estagio)
    
    dados ={
        'estagiarios': estagiario,
        'mensagem':msg
    }
   
    return dados


def cadastrado_estagiario_mais_futuro(msg):
    programa_consulta = get_object_or_404(Programa,id_programa=2)
    sede_consulta = Edital.objects.filter(id_programa_edital_id=programa_consulta)
    estagio = Estagio.objects.filter(id_edital_estagio_id__in=sede_consulta)
    estagiario = Estagiario.objects.filter(estagio_estagiario_id__in=estagio)
    
    dados ={
        'estagiarios': estagiario,
        'mensagem':msg
    }
   
    return dados

@login_required(login_url="/login/")
def criar_estagiario_mais_futuro(request):
    if request.method == "POST":
        nome_estagiario = request.POST['nome_estagiario']
        cpf = request.POST['cpf']
        rg = request.POST['rg']
        turno = request.POST['turno']
        email = request.POST['email']
        semestre = request.POST['semestre']
        nis = request.POST['nis']
        telefone = request.POST['telefone']
        responsavel = request.POST['responsavel']
        nascimento = request.POST['nascimento']
        genero = request.POST['genero']
        raca = request.POST['raca']
        bairro = request.POST['bairro']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        Matricula = request.POST['Matricula']
        situaçao = request.POST['situaçao']
        supervisor = request.POST['supervisor']
        sede = request.POST['sede']
        faculdade = request.POST['faculdade']
        estagio = request.POST['estagio']

        #validacao de error
        erros = [{"Erro": 'CPF', "Valido": True, "Mensagem": "CPF Invalido"},
                 {"Erro": 'Rg', "Valido": True, "Mensagem": "Preencher RG"},
                 {"Erro": 'Nome', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Turno', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Email', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Telefone', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Semestre', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Nascimento', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Genero', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Raca', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Situacao', "Valido": True, "Mensagem": "Preencher Nome"}]

        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)
        if len(list(ExisteErros))>0:
            print("existe erros")
        else:
            sedeObj = Sede.objects.get(id_sede=sede)
            faculdadeObj = Faculdade.objects.get(id_faculdade=faculdade)
            estagioObj = Estagio.objects.get(id_estagio=estagio)
            supervisorObj = Supervisor.objects.get(id_supervisor = supervisor)
            estagiario = Estagiario.objects.create(cpf_estagiario = cpf,
                nome_estagiario = nome_estagiario, rg_estagiario = rg,
                turno_estagiario = turno, email_estagiario = email,
                semestre_estagiario = semestre, nis_pis_estagiario = nis,
                telefone_estagiario = telefone, nome_responsavel_estagiario = responsavel,
                data_nascimento_estagiario = nascimento,
                genero_estagiario = genero, raca_estagiario = raca,
                bairro_estagiario = bairro, numero_estagiario = numero,
                complemento_estagiario = complemento, matricula_estagiario = Matricula,
                situacao_estagiario = situaçao, supervisor_estagiario = supervisorObj,
                sede_estagiario = sedeObj, faculdade_estagiario = faculdadeObj,
                estagio_estagiario = estagioObj)
            
            estagiario.save()
            msg = 'Estagiario Cadastrado com Sucesso!'
        return render(request,"home/MFES_dashboard.html",cadastrado_estagiario_mais_futuro(msg))
    else:
        return redirect("sistemaSec/templates/home/MFES_criar_estagiario.html")

@login_required(login_url="/login/")
def consultar_estagiario_mais_futuro(request):
    
    estagiarios = Estagiario.objects.all()
    
        
    if 'buscar_estagiario_partiu_estagio' in request.GET:
        nome_consulta=request.GET['buscar_estagiario_partiu_estagio']
        cpf_consulta=request.GET['buscar_cpf_estagiario_partiu_estagio']
        situacao_consulta=request.GET['buscar_situacao_estagiario_partiu_estagio']
        turno_consulta=request.GET['buscar_turno_estagiario_partiu_estagio']
        bairro_consulta=request.GET['buscar_bairro_estagiario_partiu_estagio']
        supervisor_consulta=request.GET['buscar_supervisor_estagiario_partiu_estagio']
        sede_consulta=request.GET['buscar_sede_estagiario_partiu_estagio']
        faculdade_consulta=request.GET['buscar_faculdade_estagiario_partiu_estagio']

        if consultar_estagiario_mais_futuro:
            lista_por_nome = estagiarios.filter(Q(nome_estagiario__icontains=nome_consulta))
            lista_por_cpf = lista_por_nome.filter(Q(cpf_estagiario__icontains=cpf_consulta))
            lista_por_situacao = lista_por_cpf.filter(Q(situacao_estagiario__icontains=situacao_consulta))
            lista_por_turno = lista_por_situacao.filter(Q(turno_estagiario__icontains=turno_consulta))
            lista_por_bairro = lista_por_turno.filter(Q(bairro_estagiario__icontains=bairro_consulta))
            lista_por_supervisor = lista_por_bairro.filter(Q(supervisor_estagiario__nome_supervisor__icontains=supervisor_consulta))
            lista_por_sede = lista_por_supervisor.filter(Q(sede_estagiario__nome_sede__icontains=sede_consulta))
            lista_por_faculdade = lista_por_sede.filter(Q(faculdade_estagiario__nome_faculdade__icontains=faculdade_consulta))

    dados = {
        "estagiarios": lista_por_faculdade
    }

    return render(request,"home/MFES_buscar_estagiario.html",dados)
    
@login_required(login_url="/login/")    
def editar_estagiario_mais_futuro(request,cpf_estagiario):
    estagiario = get_object_or_404(Estagiario, pk=cpf_estagiario)

    editar_estagiario_mais_futuro = { 'estagiario':estagiario }
    
    return render(request, 'home/MFES_editar_estagiario.html', editar_estagiario_mais_futuro)

@login_required(login_url="/login/")
def atualizar_estagiario_mais_futuro(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        est = Estagiario.objects.get(pk=cpf)
        est.nome_estagiario = request.POST['nome_estagiario']
        est.cpf_estagiario = cpf
        est.rg_estagiario = request.POST['rg']
        est.turno_estagiario = request.POST['turno']
        est.email_estagiario = request.POST['email']
        est.semestre_estagiario = request.POST['semestre']
        est.nis_pis_estagiario = request.POST['nis']
        est.telefone_estagiario = request.POST['telefone']
        est.nome_responsavel_estagiario = request.POST['responsavel']
        est.data_nascimento_estagiario = request.POST['nascimento']
        est.genero_estagiario = request.POST['genero']
        est.raca_estagiario = request.POST['raca']
        est.bairro_estagiario = request.POST['bairro']
        est.numero_estagiario = request.POST['numero']
        est.complemento_estagiario = request.POST['complemento']
        est.matricula_estagiario = request.POST['Matricula']
        est.situacao_estagiario = request.POST['situaçao']
        supervisor = request.POST['supervisor']
        sede = request.POST['sede']
        faculdade = request.POST['faculdade']
        estagio = request.POST['Estagio']
        erros = [{"Erro": 'CPF', "Valido": True, "Mensagem": "CPF Invalido"},
                 {"Erro": 'Rg', "Valido": True, "Mensagem": "Preencher RG"},
                 {"Erro": 'Nome', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Turno', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Email', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Telefone', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Semestre', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Nascimento', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Genero', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Raca', "Valido": True, "Mensagem": "Preencher Nome"},
                 {"Erro": 'Situacao', "Valido": True, "Mensagem": "Preencher Nome"}]

        err = filter(lambda x: x['Valido'] == False, erros)
        ExisteErros = map(lambda x: x['Erro'], err)
        if len(list(ExisteErros))>0:
            print("existe erros")
        else:
            supervisorObj = Supervisor.objects.get(id_supervisor=supervisor)
            sedeObj = Sede.objects.get(id_sede=sede)
            faculdadeObj = Faculdade.objects.get(id_faculdade=faculdade)
            estagioObj = Estagio.objects.get(id_estagio=estagio)
            est.supervisor_estagiario = supervisorObj
            est.sede_estagiario = sedeObj
            est.faculdade_estagiario = faculdadeObj
            est.estagio_estagiario = estagioObj
            est.save()
            msg = 'Estagiario Atualizado com Sucesso!'
        return render(request,"home/index.html",cadastrado_estagiario_mais_futuro(msg))
    else:
        return redirect("home/MFES_criar_estagiario.html")


