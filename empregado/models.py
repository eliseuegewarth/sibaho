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
    email = models.EmailField(max_length=100)
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

    def turnodetrabalho_hoje(self):
        return TurnoDeTrabalho.objects.filter(estagiario=self, data=date.today())

    def horasTrabalhadas_mes(self):
        turnos = self.turnos_mes_atual()
        quantidade_inicial = (date.today() - date.today());
        horas_trabalhadas = (quantidade_inicial)

        for turno in turnos:
            horas_trabalhadas = horas_trabalhadas + turno.horasTrabalhadas()
        return (':'.join(str(horas_trabalhadas).split(':')[:2]))

    def turnos_mes_atual(self):
        turnos = self.turnos_mes(date.today().month)
        return turnos;

    def turnos_mes(self, mes):
        turnos = TurnoDeTrabalho.objects.filter(estagiario=self, data__month__gte=mes, data__month__lte=mes).order_by('data')
        return turnos;

    class Meta:
        abstract = True

class Supervisor(Empregado):
    # Não precisa de nenhuma caracteristica diferente de Empregado
    pass

class Estagiario(Empregado):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    inicio_do_contrato = models.DateField('Início Contrato')
    previsao_termino_do_contrato = models.DateField('Previsão de Termino')

class TurnoDeTrabalho(models.Model):    
    estagiario = models.ForeignKey(Estagiario, on_delete=models.CASCADE)
    data = models.DateField('dia')
    entrada = models.DateTimeField('entrada')
    saida = models.DateTimeField('saida', blank=True, null=True)
    REQUIRED_FIELDS = ['estagiario', 'data', 'entrada']
    
    def __str__(self):
        return str(self.data.strftime('%d/%b'))

    def horasTrabalhadas(self):
        if(self.saida != None):
            horas_de_trabalho = (self.saida - self.entrada)
        else:
            horas_de_trabalho = (timezone.now() - self.entrada)

        return (horas_de_trabalho)

    def horasTrabalhadas_str(self):
        return (':'.join(str(self.horasTrabalhadas()).split(':')[:2]))

    def data_str(self):
        return str(self.data.strftime('%Y-%m'))

    def hora_str(self, hora):
        return str(hora.strftime('%H:%M'))

    def entrada_str(self):
        return self.hora_str(self.entrada)

    def saida_str(self):
        str_saida = ""
        if(self.saida!=None):
            str_saida = self.hora_str(self.saida)
        else:
            # Do Nothing
            pass

        return str_saida
