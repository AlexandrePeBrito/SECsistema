# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.sede.models import Sede
from sistemaSec.nte.models import NTE
from sistemaSec.municipio.models import Municipio


class SedeForm(forms.ModelForm):
    
    class Meta:
        model = Sede
        fields = "__all__"

    nome_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome da Sede",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_responsavel_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Responsável da Sede",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    bairro_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Bairro da Sede",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    email_sede = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email da Sede",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    telefone_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone da Sede",
                "class": "form-control mask-telefone",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    codigo_inep_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Código do Inep da Sede",
                "class": "form-control mask-matricula",
            }
        ))
    
    id_nte_sede = forms.ModelChoiceField(queryset=NTE.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    id_municipio_sede = forms.ModelChoiceField(queryset=Municipio.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))