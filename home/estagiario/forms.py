from django import forms
from home.estagiario.models import Estagiario
from home.supervisor.models import Supervisor
from home.faculdade.models import Faculdade
from home.sede.models import Sede
from ..edital.models import Edital
from ..programa.models import Programa
from ..curso.models import Curso

class EstagiarioForm(forms.ModelForm):
    cpf_estagiario = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF do Estagiário",
                "class": "form-control mask-cpf",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    # outros campos com as mesmas alterações...

    programa_estagiario = forms.ModelChoiceField(queryset=Programa.objects.all(), 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    edital_estagiario = forms.ModelChoiceField(queryset=Edital.objects.all(), 
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    curso_estagiario = forms.ModelChoiceField(queryset=Curso.objects.all(), 
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
        model = Estagiario
        fields = "__all__"
