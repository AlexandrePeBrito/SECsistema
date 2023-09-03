from django.db import models

from ..municipio.models import Municipio

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nome_sede = models.CharField(max_length=200, unique=True)
    codigo_inep_sede = models.CharField(max_length=8)
    telefone_sede = models.CharField(max_length=15)
    nome_responsavel_sede = models.CharField(max_length=200)
    bairro_sede = models.CharField(max_length=50)
    email_sede = models.CharField(max_length=200)
    #foreign key
    id_municipio_sede = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name="sedes")
    
    class Meta:
        db_table = 'SEDE_sede'

    def __str__(self):
        return self.nome_sede


