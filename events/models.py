from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.conf import settings
# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(default = timezone.now)
    modified = models.DateTimeField(default = timezone.now)
    class Meta:
        abstract = True
class Categoria(models.Model):
    nombre = models.CharField(max_length= 50)
    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre
class Evento(TimeStampModel):
    nombre = models.CharField(max_length=200, unique=True)
    sumario = models.TextField(max_length=255)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria)
    lugar = models.CharField(max_length=50)
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    #imagen = models.ImageField(upload_to = 'events')
    is_free = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    vistas = models.PositiveIntegerField(default=0, blank=True, null=True)
    organizador = models.ForeignKey('auth.User')

    def guardar(self):
        self.save()
    def __str__(self):
        return self.nombre
class Asistente(TimeStampModel):
    asistente = models.ForeignKey('auth.User')
    evento = models.ManyToManyField(Evento)

    atendido = models.BooleanField(default = False)
    pagado = models.BooleanField(default = False)

    def __str__(self):
        return "%s " % (self.evento.asistente)
class Participante(models.Model):
    asistente = models.ForeignKey('auth.User')
    evento = models.ForeignKey(Evento)
    def __str__(self):
        return "%s %s" % (self.evento.nombre, self.asistente.username)

class Comentario(TimeStampModel):
    usuario = models.ForeignKey('auth.User')
    evento = models.ForeignKey(Evento)

    contenido = models.TextField()
    def __str__(self):
        return "%s %s" % (self.usuario.username, self.evento.nombre)
