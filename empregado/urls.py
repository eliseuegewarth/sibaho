from django.conf.urls import url

from . import views

app_name = 'empregado'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^supervisores/$', views.supervisores, name='supervisores'),
    url(r'^supervisores/(?P<supervisor_id>[0-9]+)/$', views.supervisor, name='supervisor'),
    url(r'^supervisores/create/$', views.criarSupervisor, name='criarSupervisor'),
    url(r'^estagiarios$', views.estagiario, name='estagiario'),
    url(r'^estagiarios/new/$', views.criarEstagiario, name='criarEstagiario'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^bancodehoras/$', views.bancodehoras, name='bancodehoras'),
]