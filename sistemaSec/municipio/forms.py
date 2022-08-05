# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import CharField, ModelForm
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sistemaSec.municipio.models import Municipio
from sistemaSec.nte.models import NTE


class MunicipioForm(forms.ModelForm):
    
    class Meta:
        model = Municipio
        fields = "__all__"

    nome_municipio = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Município",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    id_nte_municipio = forms.ModelChoiceField(queryset=NTE.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))