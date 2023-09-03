# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.faculdade.models import Faculdade
from sistemaSec.sede.models import Sede
from ..edital.models import Edital
from ..programa.models import Programa
from ..curso.models import Curso

class EstagiarioForm(forms.ModelForm):
    
    class Meta:
        model = Estagiario
        fields = "__all__"

    requerido = "required oninvalid"
    campo_requerido = "this.setCustomValidity('Campo requerido')" 
    onchange = "onchange"
    campo_requerido_empty = "this.setCustomValidity('')"

    cpf_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "CPF do Estagiário",
                "class": "form-control mask-cpf",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    nome_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Estagiário",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
        
    rg_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "RG do Estagiário",
                "class": "form-control mask-rg",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    
    turno = (
        ("","Selecione"),
        ("Matutino","Matutino"),
        ("Vespertino","Vespertino"))
    turno_estagiario = forms.ChoiceField(choices=turno, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    email_estagiario = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email do Estagiário",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    semestres = (
        ("","Selecione"),
        ("1","1"),("2","2"),
        ("3","3"),("4","4"),
        ("5","5"),("6","6"),
        ("7","7"),("8","8"),
        ("9","9"),("10","10")
        )
    semestre_estagiario = forms.ChoiceField(choices=semestres, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    nis_pis_estagiario = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "NIS do Estagiário",
                "class": "form-control mask-nis",
            }
        ))

    telefone_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone do Estagiário",
                "class": "form-control mask-telefone",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    nome_responsavel_estagiario = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Responsável",
                "class": "form-control",
            }
        ))

    data_nascimento_estagiario = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Data de nascimento",
                "class": "form-control mask-data",

            }
        ))

    genero = (
        ("","Selecione"),
        ('Masculino','Masculino'),
        ('Feminino','Feminino'))
    genero_estagiario = forms.ChoiceField(choices=genero, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    
    raca = (
        ("","Selecione"),
        ("Branca","Branca"),
        ("Preta","Preta"),
        ("Parda","Parda"),
        ("Amarela","Amarela"),
        ("Indigena","Indigena"))
    raca_estagiario = forms.ChoiceField(choices=raca, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    bairro_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Bairro",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    numero_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Número",
                "class": "form-control mask-matricula",
            }
        ))

    complemento_estagiario = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Complemento",
                "class": "form-control",
            }
        ))

    matricula_estagiario = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Matrícula do Estagiário",
                "class": "form-control mask-matricula",
            }
        ))

    situacao = (
        ("","Selecione"),
        ("Ativo","Ativo"),
        ("Desligado","Desligado"),
        ("Desclassificado","Desclassificado"))
    situacao_estagiario = forms.ChoiceField(choices=situacao, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
   
    supervisor_estagiario = forms.ModelChoiceField(queryset=Supervisor.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    sede_estagiario = forms.ModelChoiceField(queryset=Sede.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    
    faculdade_estagiario = forms.ModelChoiceField(queryset=Faculdade.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    programa_estagiario = forms.ModelChoiceField(queryset=Programa.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    
    edital_estagiario = forms.ModelChoiceField(queryset=Edital.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    curso_estagiario = forms.ModelChoiceField(queryset=Curso.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    
   