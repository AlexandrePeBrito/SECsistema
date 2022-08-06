# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.edital.models import Edital
from sistemaSec.programa.models import Programa


class EditalForm(forms.ModelForm):
    
    class Meta:
        model = Edital
        fields = "__all__"

    requerido = "required oninvalid"
    campo_requerido = "this.setCustomValidity('Campo requerido')" 

    id_edital = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Código do Edital",
                "class": "form-control",
                requerido: campo_requerido
            }
        ))
    quantidade_vagas_edital = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Quantidade de Vagas",
                "class": "form-control mask-matricula",
                requerido: campo_requerido
            }
        ))

    id_programa_edital = forms.ModelChoiceField(queryset=Programa.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                requerido: campo_requerido
            }
        ))