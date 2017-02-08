from datetime import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class RamalModel(models.Model):
    regex_ramal = RegexValidator(regex=r'^\d{4}$', message="Numero de telefone precisa estar no formato: XXXX ")
    numero_ramal = models.CharField(max_length=4, validators=[regex_ramal], blank=True)

    def __str__(self):
        return self.numero_ramal

class Empregado(models.Model):
    nome_completo = models.CharField(max_length=100)
    nome_de_usuario = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    lotacao = models.CharField(max_length=100)
    ramal = models.ForeignKey(RamalModel, on_delete=models.CASCADE)
    REQUIRED_FIELDS = [
        'nome_completo',
        'password',
        'nome_de_usuario',
        'email',
        'lotacao',
        'ramal'
    ]
    def __str__(self):
        return self.nome_completo
    class Meta:
        abstract = True


class Supervisor(Empregado):
    pass


class Estagiario(Empregado):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)


class TurnoDeTrabalho(models.Model):    
    estagiario = models.ForeignKey(Estagiario, on_delete=models.CASCADE)
    data = models.DateField('dia')
    entrada = models.DateTimeField('entrada')
    saida = models.DateTimeField('saida', blank=True, null=True)
    REQUIRED_FIELDS = ['estagiario', 'data', 'entrada']
    
    def __str__(self):
        return str(self.data)

    def horasTrabalhadas(self):
        if(self.saida != None):
            horas_de_trabalho = (self.saida - self.entrada)
        else:
            horas_de_trabalho = (timezone.now() - self.entrada)

        return (':'.join(str(horas_de_trabalho).split(':')[:2]))