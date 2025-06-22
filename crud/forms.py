from django import forms
from .models import Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'dataNascimento']
        widgets = {
            'dataNascimento': forms.DateTimeInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }


        