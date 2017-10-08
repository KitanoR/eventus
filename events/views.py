from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Categoria, Evento ,Asistente, Comentario, Participante
# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.all().order_by('-created')[:6]
    categorias = Categoria.objects.all()
    
    return render(request, 'events/listareventos.html',{'eventos': eventos, 'categorias':categorias})
