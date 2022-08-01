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
        fields = '__all__'

    nome_direitor_NTE =  forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Direitor",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    telefone_NTE = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone do NTE",
                "class": "form-control mask-telefone",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    email_NTE = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email do NTE",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
   