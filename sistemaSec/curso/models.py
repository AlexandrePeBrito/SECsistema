from django.db import models

class Curso(models.Model):
    id_curso =  models.AutoField(primary_key=True)
    nome_curso = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'CUSO_curso'

    def __str__(self):
        return self.nome_curso

        
        