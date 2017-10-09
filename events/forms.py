from django import forms
from .models import Categoria, Evento ,Asistente, Comentario, Participante

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('nombre', 'sumario','contenido','categoria','lugar','inicio','final','imagen','is_free','precio',)
