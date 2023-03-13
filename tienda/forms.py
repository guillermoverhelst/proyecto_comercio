from django import forms
from tienda.models import usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model  = usuario
        fields  = '__all__'

class InicioSesionForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ["correo","clave"]