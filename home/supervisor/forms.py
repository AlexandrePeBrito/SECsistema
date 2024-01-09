from django import forms
from home.sede.models import Sede
from home.supervisor.models import Supervisor

class SupervisorForm(forms.ModelForm):
    
    nome_supervisor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Supervisor",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    email_supervisor = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email do Supervisor",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    telefone_supervisor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone do Supervisor",
                "class": "form-control mask-telefone",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )
    
    sede_supervisor = forms.ModelChoiceField(queryset=Sede.objects.all(), 
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
        model = Supervisor
        fields = "__all__"
