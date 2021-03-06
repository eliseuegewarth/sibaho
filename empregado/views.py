from datetime import date
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Supervisor, Estagiario

def index(request):
    return render(request, 'empregado/index.html')

def contact(request):
    return render(request, 'empregado/base.html')

def login(request):

    try:
        form_nome_de_usuario = request.POST['nome_de_usuario']
        form_password = request.POST['password']

    except(KeyError):

        return render(request, 'empregado/login.html', {
                'error_message': 'Preencha todos os campos.', 
            })
    else:
        usuario = Supervisor.objects.get(nome_de_usuario=form_nome_de_usuario)
        if(usuario==None):
            if(usuario.password == form_password):
                return HttpResponseRedirect(reverse('empregado:index'))
        return render(request, 'empregado/login.html', {
                'error_message': 'Usuário ou senha incorretos.', 
            })

def supervisores(request):
    lista_supervisores = Supervisor.objects.order_by('nome_completo')
    conteudo =  {'lista_supervisores': lista_supervisores}
    return render(request, 'empregado/supervisores.html', conteudo)

def supervisor(request, supervisor_id):
    supervisor = get_object_or_404(Supervisor, pk = supervisor_id)
    return render(request, 'empregado/supervisor.html', {'supervisor': supervisor})

def criarSupervisor(request):
    try:
        form_nome_completo = request.POST['nome_completo']
        form_nome_de_usuario = request.POST['nome_de_usuario']
        form_email = request.POST['email']
        form_password = request.POST['password']

    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'empregado/novo_supervisor.html', {
            'error_message': "Preencha todos os campos.",
        })
    else:
        supervisor = Supervisor(nome_completo = form_nome_completo, nome_de_usuario = form_nome_de_usuario, email=form_email, password = form_password)
        supervisor.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('empregado:supervisores'))

def estagiarios(request):
    lista_estagiarios = Estagiario.objects.order_by('nome_completo')
    conteudo =  {'lista_estagiarios': lista_estagiarios}
    return render(request, 'empregado/estagiarios.html', conteudo)

def estagiario(request, estagiario_id):
    estagiario = get_object_or_404(Estagiario, pk = estagiario_id)
    data = str(timezone.now().strftime('%Y-%m'))
    conteudo = {'estagiario': estagiario, 'data': data}
    return render(request, 'empregado/estagiario.html', conteudo)

def criarEstagiario(request):
    return HttpResponse("<html><title>Novo Estagiario</title><body>Hello, world. You're at the empregado index.</body></html>")

def bancodehoras(request):
    return render(request, 'empregado/bancodehoras.html')

def turnodetrabalho(request, estagiario_id, turnodetrabalho_id):
    return render(request, 'empregado/turnodetrabalho.html')

def mes(request, estagiario_id, data):
    return render(request, 'empregado/turnodetrabalho.html')

def relatorio(request, estagiario_id):
    estagiario = get_object_or_404(Estagiario, pk = estagiario_id)
    data = str(date.today().strftime('%Y-%m'))
    conteudo = { 'estagiario': estagiario,
                 'data': data,
                }

    return render(request, 'empregado/relatorio_estagiario.html', conteudo)
