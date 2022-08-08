from django.db import models
from ..programa.models import Programa

class Edital(models.Model):
    id_edital = models.CharField(primary_key=True, max_length=7)
    quantidade_vagas_edital = models.IntegerField()
    #foreign key
    def __str__(self):
        return self.id_edital

