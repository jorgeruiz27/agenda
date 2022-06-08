from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    local_evento = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #CASCADE se o usario for excluido será excluido todos o eventos deste usuario

    class Meta:
        db_table = 'evento' #Nome da Tabela

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y às %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
    def get_evento_proximo(self):
        data_atual = datetime.now()
        data_proxima = datetime.now() + timedelta(hours=1)
        #console.log("teste")
        if (self.data_evento > data_atual) and (self.data_evento <= data_proxima):
            return True
        else:
            return False