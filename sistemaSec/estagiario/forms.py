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


class EstagiarioForm(forms.ModelForm):
    
    class Meta:
        model = Estagiario
        fields = '__all__'

    cpf_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "CPF do Estagiario",
                "class": "form-control mask-cpf",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Estagiario",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
        
    rg_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "RG do Estagiario",
                "class": "form-control mask-rg",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    turno = (
        ("------","------"),
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
                "placeholder": "Email do Estagiario",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    semestres = (
        ("------","------"),
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
                "placeholder": "NIS do Estagiario",
                "class": "form-control mask-nis",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    telefone_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone do Estagiario",
                "class": "form-control mask-telefone",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_responsavel_estagiario = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Responsavel",
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
        ("------","------"),
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
        ("------","------"),
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
                "placeholder": "Numero",
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
                "placeholder": "Matricula do Estagiario",
                "class": "form-control mask-matricula",
            }
        ))

    situacao = (
        ("------","------"),
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
   