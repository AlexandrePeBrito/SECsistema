from django.db import models

class Faculdade(models.Model):
    id_faculdade = models.AutoField(primary_key=True)
    nome_faculdade = models.CharField(max_length=200)
    cnpj_faculdade = models.CharField(max_length=18)
    nome_direitor_faculdade = models.CharField(max_length=100)
    telefone_faculdade = models.CharField(max_length=15)
    campus_faculdade = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'FACU_faculdade'

    def __str__(self):
        return self.nome_faculdade
