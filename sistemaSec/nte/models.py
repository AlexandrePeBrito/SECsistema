from django.db import models

class NTE(models.Model):
    id_NTE = models.AutoField(primary_key=True)
    nome_direitor_NTE = models.CharField(max_length=100)
    telefone_NTE = models.CharField(max_length=15)
    email_NTE = models.CharField(max_length=100)
        
    class Meta:
        db_table = 'NTE_nte'

    def __str__(self):
        return str(self.id_NTE)


