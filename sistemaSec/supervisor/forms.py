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
from sistemaSec.supervisor.models import Supervisor

class SupervisorForm(forms.ModelForm):
    
    class Meta:
        model = Supervisor
        fields = '__all__'

    nome_supervisor = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Nome do Supervisor",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    email_supervisor = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Email do Supervisor",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    telefone_supervisor = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Telefone do Supervisor",
                "class": "form-control mask-telefone",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    """ sede_supervisor = forms.ModelChoiceField(queryset=0, 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        )) """
    
        
   
   