from django.db import models
from ..edital.models import Edital

class Programa(models.Model):
    id_programa = models.AutoField(primary_key=True)
    nome_programa = models.CharField(max_length=100)
    
    #FOREIGN KEY
    edital_estagiario = models.ForeignKey(Edital, on_delete=models.PROTECT, related_name="edital", null = True)

    class Meta:
        db_table = 'PROG_programa'

    def __str__(self):
        return self.nome_programa