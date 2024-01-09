from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from home.faculdade.models import Faculdade
from .forms import FaculdadeForm

url_criar_faculdade = "home/FACU_criar_faculdade.html"
url_dashboard_faculdade = "home/FACU_dashboard.html"
url_editar_faculdade = "home/FACU_editar_faculdade.html"

@login_required(login_url="/login/")
def criar_faculdade(request):
    if request.method == "GET":
        form = FaculdadeForm()
        return render(request, url_criar_faculdade, {"form": form})
        
    if request.method == "POST":
        form = FaculdadeForm(request.POST)
        if form.is_valid():
            nome_faculdade = form.cleaned_data.get("nome_faculdade")
            cnpj_faculdade = form.cleaned_data.get("cnpj_faculdade")
            diretor_faculdade = form.cleaned_data.get("nome_diretor_faculdade")
            campus = form.cleaned_data.get("campus_faculdade")
            telefone = form.cleaned_data.get("telefone_faculdade")
        
            faculdade = Faculdade.objects.create(
                nome_faculdade=nome_faculdade,
                cnpj_faculdade=cnpj_faculdade,
                nome_diretor_faculdade=diretor_faculdade,
                telefone_faculdade=telefone,
                campus_faculdade=campus
            )
        
            faculdade.save()
            msg = "Faculdade cadastrada com sucesso!"
            return render(request, url_dashboard_faculdade, {"mensagem": msg})
        
        msg = "Ocorreu um erro no cadastro!"
        return render(request, url_dashboard_faculdade, cadastrado_faculdade(form, msg))

@login_required(login_url="/login/")
def consultar_faculdade(request):
    lista_por_nome = None
    faculdades = Faculdade.objects.all()
    
    if "buscar_faculdade" in request.GET:
        nome_consulta = request.GET["buscar_faculdade"]
        lista_por_nome = faculdades.filter(Q(nome_faculdade__icontains=nome_consulta))
            
    if lista_por_nome:
        dados = {
            "faculdades": lista_por_nome,
            "error": False,
            "mensagem": "Consulta feita com sucesso!"
        }
    else:
        dados = {
            "faculdades": lista_por_nome,
            "error": True,
            "mensagem": "Nenhuma faculdade localizada!"
        }
    return render(request, url_dashboard_faculdade, dados)
    
@login_required(login_url="/login/")    
def editar_faculdade(request, id_faculdade):
    faculdade = get_object_or_404(Faculdade, id_faculdade=id_faculdade)
    form = FaculdadeForm(instance=faculdade)

    if request.method == "POST":
        form = FaculdadeForm(request.POST, instance=faculdade)

        if form.is_valid():
            faculdade.save()
            msg = "Faculdade alterada com sucesso!"
            return render(request, url_dashboard_faculdade, {"mensagem": msg})

        msg = "Ocorreu um erro!"
        return render(request, url_dashboard_faculdade, cadastrado_faculdade(form, msg))
    else:
        return render(request, url_editar_faculdade, {"faculdade": faculdade, "form": form})

def cadastrado_faculdade(form, msg):
    faculdades = Faculdade.objects.all()
    dados = {
        "faculdades": faculdades,
        "form": form,
        "mensagem": msg
    }
    return dados
