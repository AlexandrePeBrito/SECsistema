from django import forms
from home.faculdade.models import Faculdade

class FaculdadeForm(forms.ModelForm):
    nome_faculdade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome da Faculdade",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo Obrigatório')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    cnpj_faculdade = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "CNPJ da Faculdade",
                "class": "form-control mask-cnpj",
            }
        )
    )
    nome_direitor_faculdade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Diretor da Faculdade",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo Obrigatório')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    telefone_faculdade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone da Faculdade",
                "class": "form-control mask-telefone",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo Obrigatório')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    campus_faculdade = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Campus da Faculdade",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Faculdade
        fields = "__all__"
