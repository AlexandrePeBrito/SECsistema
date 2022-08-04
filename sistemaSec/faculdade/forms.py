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

    nome_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome da Faculdade",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    cnpj_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "CNPJ da Faculdade",
                "class": "form-control mask-cnpj",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    nome_direitor_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Direitor da Faculdade",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    telefone_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone da Faculdade",
                "class": "form-control mask-telefone",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    campus_faculdade = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Campus da Faculdade",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))