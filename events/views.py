from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Categoria, Evento ,Asistente, Comentario, Participante
from django.contrib.auth.decorators import login_required

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.all().order_by('-created')
    categorias = Categoria.objects.all()

    return render(request, 'events/listareventos.html',{'eventos': eventos, 'categorias':categorias})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    comentarios = Comentario.objects.filter(evento__pk = pk)
    return render(request, 'events/detalleevento.html',{'evento': evento, 'comentarios':comentarios})

def unirse_evento(request, pk):
    p = Participante(asistente= request.user,evento = Evento.objects.get(pk = pk))
    p.guardar()
    return redirect('home')
def mis_clases(request):
    eventos = Evento.objects.filter(organizador__pk = request.user.pk)
    return render(request, 'events/misclase.html' , {'eventos': eventos})
def mis_prox_eventos(request):
    actividades = Participante.objects.filter(asistente__pk = request.user.pk)
    return render(request,'events/actividadesprox.html', {'actividades':actividades})
