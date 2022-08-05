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
from sistemaSec.edital.models import Edital
from sistemaSec.curso.models import Curso


class EstagioForm(forms.ModelForm):
    
    class Meta:
        model = Estagio
        fields = "__all__"

    carga_horaria_estagio = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Carga Horária do Estágio",
                "class": "form-control mask-matricula",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    area_estagio = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Setor do Estágio",
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))

    id_edital_estagio = forms.ModelChoiceField(queryset=Edital.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    
    id_cursos_estagio = forms.ModelChoiceField(queryset=Curso.objects.all(), 
        widget = forms.Select(
            attrs = {
                "class": "form-control",
                "required oninvalid" : "this.setCustomValidity('Campo requerido')"
            }
        ))
    