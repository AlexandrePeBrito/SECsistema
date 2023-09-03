from django.db import models
from ..sede.models import Sede

class Supervisor(models.Model):
    id_supervisor = models.AutoField(primary_key=True)
    nome_supervisor = models.CharField(max_length=200)
    telefone_supervisor = models.CharField(max_length=15)
    email_supervisor = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'SUPE_supervisor'

    def __str__(self):
        return self.nome_supervisor

