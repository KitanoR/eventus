from django.conf.urls import include,url #se agrega include
from . import views

urlpatterns = [
    url(r'^$',views.listar_eventos), #se redirecciona a la url del blog
    #url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub, name = 'postea'), #se redirecciona a la url del blog

]
