from django.conf.urls import url

from . import views

app_name = 'empregado'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^supervisores/$', views.supervisores, name='supervisores'),
    url(r'^supervisores/(?P<supervisor_id>[0-9]+)/$', views.supervisor, name='supervisor'),
    url(r'^supervisores/create/$', views.criarSupervisor, name='criarSupervisor'),
    url(r'^estagiarios$', views.estagiarios, name='estagiarios'),
    url(r'^estagiarios/(?P<estagiario_id>[0-9]+)$', views.estagiario, name='estagiario'),
    url(r'^estagiarios/(?P<estagiario_id>[0-9]+)/relatorio$', views.relatorio, name='relatorio'),
    url(r'^estagiarios/(?P<estagiario_id>[0-9]+)/turnodetrabalho/(?P<turnodetrabalho_id>[0-9]+)$', views.turnodetrabalho, name='turnodetrabalho'),
    url(r'^estagiarios/(?P<estagiario_id>[0-9]+)/mes/(?P<data>[0-9]+-[0-9]+)$', views.mes, name='mes'),
    url(r'^estagiarios/create/$', views.criarEstagiario, name='criarEstagiario'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^bancodehoras/$', views.bancodehoras, name='bancodehoras'),
]