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


class SedeForm(forms.ModelForm):
    
    class Meta:
        model = Sede
        fields = '__all__'

    nome_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Municipio",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_responsavel_sede = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Responsavel da Sede",
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
                "placeholder": "Codigo do Inep da Sede",
                "class": "form-control mask-matricula",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))