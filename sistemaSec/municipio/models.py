from django.db import models
from ..nte.models import NTE

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nome_municipio = models.CharField(max_length=200)
    #foreign key
    id_nte_municipio = models.ForeignKey(NTE, on_delete=models.PROTECT, related_name="municipios")

    class Meta:
        db_table = 'MUNI_municipio'

    def __str__(self):
        return self.nome_municipio
