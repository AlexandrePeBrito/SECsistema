# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.nte.models import NTE


class NTEForm(forms.ModelForm):
    
    class Meta:
        model = NTE
        fields = "__all__"

    requerido = "required oninvalid"
    campo_requerido = "this.setCustomValidity('Campo requerido')"  
    onchange = "onchange"
    campo_requerido_empty = "this.setCustomValidity('')"

    nome_direitor_NTE =  forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Diretor",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    telefone_NTE = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone do NTE",
                "class": "form-control mask-telefone",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))

    email_NTE = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email do NTE",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        ))
   