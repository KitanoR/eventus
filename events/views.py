from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Categoria, Evento ,Asistente, Comentario, Participante
from django.contrib.auth.decorators import login_required
from .forms import EventoForm, ComentarioForm
# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.all().order_by('-created')
    categorias = Categoria.objects.all()

    return render(request, 'events/listareventos.html',{'eventos': eventos, 'categorias':categorias})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    comentarios = Comentario.objects.filter(evento__pk = pk)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit = False)
            comentario.evento = evento
            comentario.usuario = request.user
            comentario.save()
            return render(request, 'events/detalleevento.html',{'evento': evento, 'comentarios':comentarios, 'form':form})
    else:
        form = ComentarioForm()

    return render(request, 'events/detalleevento.html',{'evento': evento, 'comentarios':comentarios, 'form':form})

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

def evento_nuevo(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit = False)
            evento.organizador = request.user
            evento.save()
            return redirect('detEvento', pk = evento.pk)
    else:
        form = EventoForm()
    return render(request, 'events/evento_edit.html',{'form': form})
def evento_editar(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance = evento)
        if form.is_valid():
            evento = form.save(commit = False)
            evento.organizador = request.user
            evento.save()
            return redirect('detEvento', pk = evento.pk)
    else:
        form = EventoForm(instance = evento)
    return render(request, 'events/evento_edit.html',{'form': form})
def evento_eliminar(request, pk):
    evento = get_object_or_404(Evento, pk = pk)
    evento.delete()
    return redirect('miseventos')
def salir_evento(request, pk):
    partpante = get_object_or_404(Participante, pk = pk)
    participante.delete()
    return redirect('participar')
def comentario_eliminar(request, pk):
    comentario = get_object_or_404(Comentario, pk = pk)
    comentario.delete()
    return redirect('miseventos')
