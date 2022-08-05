# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.estagiario.models import Estagiario
from sistemaSec.supervisor.models import Supervisor
from sistemaSec.estagio.models import Estagio
from sistemaSec.faculdade.models import Faculdade
from sistemaSec.sede.models import Sede

class EstagiarioForm(forms.ModelForm):
    
    class Meta:
        model = Estagiario
        fields = "__all__"

    cpf_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "CPF do Estagiário",
                "class": "form-control mask-cpf",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Estagiário",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
        
    rg_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "RG do Estagiário",
                "class": "form-control mask-rg",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    turno = (
        ("0","Selecione"),
        ("Matutino","Matutino"),
        ("Vespertino","Vespertino"))
    turno_estagiario = forms.ChoiceField(choices=turno, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    email_estagiario = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email do Estagiário",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    semestres = (
        ("0","Selecione"),
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
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nis_pis_estagiario = forms.CharField(
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
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_responsavel_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Responsável",
                "class": "form-control",
            }
        ))

    data_nascimento_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Data de nascimento",
                "class": "form-control mask-data",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    genero = (
        ("0","Selecione"),
        ('Masculino','Masculino'),
        ('Feminino','Feminino'))
    genero_estagiario = forms.ChoiceField(choices=genero, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    raca = (
        ("0","Selecione"),
        ("Branca","Branca"),
        ("Preta","Preta"),
        ("Parda","Parda"),
        ("Amarela","Amarela"),
        ("Indigena","Indigena"))
    raca_estagiario = forms.ChoiceField(choices=raca, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    bairro_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Bairro",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    numero_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Número",
                "class": "form-control mask-matricula",
            }
        ))

    complemento_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Complemento",
                "class": "form-control",
            }
        ))

    matricula_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Matrícula do Estagiário",
                "class": "form-control mask-matricula",
            }
        ))

    situacao = (
        ("0","Selecione"),
        ("Ativo","Ativo"),
        ("Desligado","Desligado"),
        ("Desclassificado","Desclassificado"))
    situacao_estagiario = forms.ChoiceField(choices=situacao, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
   
    supervisor_estagiario = forms.ModelChoiceField(queryset=Supervisor.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    sede_estagiario = forms.ModelChoiceField(queryset=Sede.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    faculdade_estagiario = forms.ModelChoiceField(queryset=Faculdade.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    estagio_estagiario = forms.ModelChoiceField(queryset=Estagio.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))