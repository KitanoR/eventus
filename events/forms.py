from django import forms
from .models import Categoria, Evento ,Asistente, Comentario, Participante
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nombre',
            'sumario',
            'contenido',
            'categoria',
            'lugar',
            'inicio',
            'final',
            'imagen',
            'is_free',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre',
            'sumario':'Sumario',
            'contenido': 'Contenido',
            'categoria': 'Categoria',
            'lugar': 'Lugar',
            'inicio': 'Inicio',
            'final': 'Final',
            'imagen': 'Imagen',
            'is_free': 'Gratis',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs ={'class': 'form-control'}),
            'sumario': forms.Textarea(attrs = {'class': 'form-control'}),
            'contenido': forms.Textarea(attrs = {'class': 'form-control'}),
            'categoria': forms.Select(attrs = {'class': 'form-control'}),
            'lugar': forms.TextInput(attrs = {'class': 'form-control'}),
            'inicio': forms.DateInput(format = ('%d-%m-%Y'), attrs = {'class': 'form-control','placeholder':'Seleccione una fecha'}),
            'final': forms.DateInput(format = ('%d-%m-%Y'), attrs = {'class': 'form-control','placeholder':'Seleccione una fecha'}),
        }
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)


class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels={
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }
        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs = {'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs = {'class': 'form-control'}),
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password',]
        labels = {
            'username':'Usuario',
            'password':'Contraseña',
        }
        widgets = {
            'username' : forms.TextInput(attrs = {'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs = {'class': 'form-control'}),
        }
