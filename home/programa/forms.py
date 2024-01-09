from django import forms
from home.programa.models import Programa

class ProgramaForm(forms.ModelForm):
    
    nome_programa = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Programa",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    class Meta:
        model = Programa
        fields = "__all__"
