# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.faculdade.models import Faculdade


class FaculdadeForm(forms.ModelForm):
    
    class Meta:
        model = Faculdade
        fields = "__all__"

    requerido = "required oninvalid"
    campo_requerido = "this.setCustomValidity('Campo Obrigatorio')"
    onchange = "onchange"
    campo_requerido_empty = "this.setCustomValidity('')"

    nome_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome da Faculdade",
                "class": "form-control",
                requerido : campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
    cnpj_faculdade = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "CNPJ da Faculdade",
                "class": "form-control mask-cnpj",
            }
        ))

    nome_direitor_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Diretor da Faculdade",
                "class": "form-control",
                requerido : campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    telefone_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone da Faculdade",
                "class": "form-control mask-telefone",
                requerido : campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    campus_faculdade = forms.CharField(required = False,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Campus da Faculdade",
                "class": "form-control",
            }
        ))