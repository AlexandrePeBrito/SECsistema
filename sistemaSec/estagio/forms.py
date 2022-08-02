# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.estagio.models import Estagio


class EstagioForm(forms.ModelForm):
    
    class Meta:
        model = Estagio
        fields = '__all__'

    carga_horaria_estagio = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Carga Horaria do Estágio",
                "class": "form-control mask-matricula",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    area_estagio = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Setor do Estagio",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    