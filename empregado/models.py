from django.db import models
from datetime import datetime

class Empregado(models.Model):
    nome_completo = models.CharField(max_length=100)
    nome_de_usuario = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['nome_completo', 'password', 'nome_de_usuario', 'email']
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

        return str(horas_de_trabalho)