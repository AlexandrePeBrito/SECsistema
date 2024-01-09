from django import forms
from home.edital.models import Edital

class EditalForm(forms.ModelForm):
    id_edital = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Código do Edital",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    quantidade_vagas_edital = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Quantidade de Vagas",
                "class": "form-control mask-matricula",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    class Meta:
        model = Edital
        fields = "__all__"
