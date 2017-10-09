from django.conf.urls import include,url #se agrega include
from . import views

urlpatterns = [
    url(r'^$',views.listar_eventos, name='home'), #se redirecciona a la url del blog
    url(r'^comentario/(?P<pk>[0-9]+)/$', views.detalle_evento, name = 'detEvento'), #se redirecciona a la url del blog
    url(r'^inscripcion/(?P<pk>[0-9]+)/$', views.unirse_evento, name = 'participar'), #se redirecciona a la url del blog
    url(r'^miseventos/$', views.mis_clases, name = 'miseventos'), #se redirecciona a la url del blog
    url(r'^misactividades/$', views.mis_prox_eventos, name = 'misactividades'), #se redirecciona a la url del blog

]
