from django.db import models
from ..edital.models import Edital
from ..programa.models import Programa
from ..curso.models import Curso

class Estagio(models.Model):
    id_estagio = models.AutoField(primary_key=True)
    carga_horaria_estagio = models.IntegerField()
    area_estagio = models.CharField(max_length=200)
    #foreign key
    id_edital_estagio = models.ForeignKey(Edital, on_delete=models.PROTECT, related_name="estagios")
    id_cursos_estagio = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="estagios")
    
    def __str__(self):
        return self.area_estagio
