from django import forms
from home.curso.models import Curso

class CursoForm(forms.ModelForm):
    nome_curso = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Curso",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    class Meta:
        model = Curso
        fields = "__all__"
