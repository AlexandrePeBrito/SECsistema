from django import forms
from home.sede.models import Sede
from home.nte.models import NTE
from home.municipio.models import Municipio

class SedeForm(forms.ModelForm):
    
    nome_sede = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome da Sede",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    nome_responsavel_sede = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Responsável da Sede",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    bairro_sede = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bairro da Sede",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    email_sede = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email da Sede",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    telefone_sede = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone da Sede",
                "class": "form-control mask-telefone",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    codigo_inep_sede = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Código do Inep da Sede",
                "class": "form-control mask-matricula",
            }
        )
    )

    id_nte_sede = forms.ModelChoiceField(queryset=NTE.objects.all(), 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    id_municipio_sede = forms.ModelChoiceField(queryset=Municipio.objects.all(), 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    class Meta:
        model = Sede
        fields = "__all__"
