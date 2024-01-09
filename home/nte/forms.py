from django import forms
from home.nte.models import NTE

class NTEForm(forms.ModelForm):
    
    nome_direitor_NTE = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Diretor",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    telefone_NTE = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone do NTE",
                "class": "form-control mask-telefone",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    email_NTE = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email do NTE",
                "class": "form-control",
                "required": True,
                "oninvalid": "this.setCustomValidity('Campo requerido')",
                "onchange": "this.setCustomValidity('')",
            }
        )
    )

    class Meta:
        model = NTE
        fields = "__all__"
