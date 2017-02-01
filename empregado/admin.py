from django.contrib import admin

from .models import Supervisor, Estagiario, TurnoDeTrabalho

admin.site.register(Supervisor)
admin.site.register(Estagiario)
admin.site.register(TurnoDeTrabalho)