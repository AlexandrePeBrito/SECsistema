from django import forms
from home.municipio.models import Municipio
from home.nte.models import NTE

class MunicipioForm(forms.ModelForm):
    requerido = "required oninvalid"
    campo_requerido = "this.setCustomValidity('Campo requerido')" 
    onchange = "onchange"
    campo_requerido_empty = "this.setCustomValidity('')"

    nome_municipio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Município",
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        )
    )
    
    id_nte_municipio = forms.ModelChoiceField(
        queryset=NTE.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                requerido: campo_requerido,
                onchange: campo_requerido_empty
            }
        )
    )

    class Meta:
        model = Municipio
        fields = "__all__"
