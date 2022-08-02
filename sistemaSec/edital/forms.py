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


class EditalForm(forms.ModelForm):
    
    class Meta:
        model = Edital
        fields = '__all__'

    id_edital = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Codigo do Edital",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    quantidade_vagas_edital = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Quantidade de Vagas do Edital",
                "class": "form-control mask-matricula",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
