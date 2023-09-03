from django.db import models

class Edital(models.Model):
    id_edital = models.CharField(primary_key=True, max_length=7)
    quantidade_vagas_edital = models.IntegerField()
    
    class Meta:
        db_table = 'EDTL_edital'

    def __str__(self):
        return self.id_edital

