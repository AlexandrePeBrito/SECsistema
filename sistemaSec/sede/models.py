from django.db import models
from ..nte.models import NTE
from ..municipio.models import Municipio

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nome_sede = models.CharField(max_length=200)
    codigo_inep_sede = models.CharField(max_length=8)
    telefone_sede = models.CharField(max_length=12)
    nome_responsavel_sede = models.CharField(max_length=200)
    bairro_sede = models.CharField(max_length=50)
    email_sede = models.CharField(max_length=200)
    #foreign key
    id_nte_sede = models.ForeignKey(NTE, on_delete=models.PROTECT, related_name="sedes")
    id_municipio_sede = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name="sedes")


