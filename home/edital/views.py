from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditalForm
from .models import Edital
from django.db.models import Q

@login_required(login_url="/login/")
def criar_edital(request):
    form = EditalForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Edital Cadastrado com Sucesso!"
            return render(request, "home/EDTL_dashboard.html", {"form": form, "mensagem": msg})

        msg = "Ocorreu um Error!"
        return render(request, "home/EDTL_dashboard.html", {"form": form, "mensagem": msg})
    else:
        return render(request, "home/EDTL_criar_edital.html", {"form": form})

@login_required(login_url="/login/")
def consultar_edital(request):
    lista_por_edital = None
    editais = Edital.objects.all()

    if "buscar_edital" in request.GET:
        edital_consulta = request.GET["buscar_edital"]
        if edital_consulta:
            lista_por_edital = editais.filter(Q(id_edital__icontains=edital_consulta))

    if lista_por_edital:
        return render(request, "home/EDTL_dashboard.html", {"editais": lista_por_edital, "error": False, "mensagem": "Consulta Feita com Sucesso!"})
    else:
        return render(request, "home/EDTL_dashboard.html", {"editais": lista_por_edital, "error": True, "mensagem": "Nenhum Edital Localizado!"})

@login_required(login_url="/login/")    
def editar_edital(request, id_edital):
    edital = Edital.objects.get(id_edital=id_edital)
    form = EditalForm(request.POST or None, instance=edital)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Edital Alterado com sucesso!"
            return render(request, "home/EDTL_dashboard.html", {"form": form, "mensagem": msg})
        
        msg = "Ocorreu um Erro"
        return render(request, "home/EDTL_dashboard.html", {"form": form, "mensagem": msg})
    else:
        return render(request, "home/EDTL_editar_edital.html", {"edital": edital, "form": form})
