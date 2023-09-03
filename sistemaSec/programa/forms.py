# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.programa.models import Programa


class ProgramaForm(forms.ModelForm):
    
    class Meta:
        model = Programa
        fields = "__all__"

    nome_programa = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Programa",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')",
                "onchange" : "this.setCustomValidity('')"
            }
        ))