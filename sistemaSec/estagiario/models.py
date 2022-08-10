"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from cpf_field.models import CPFField
from ..supervisor.models import Supervisor
from ..faculdade.models import Faculdade
from ..sede.models import Sede
from ..edital.models import Edital
from ..programa.models import Programa
from ..curso.models import Curso


class Estagiario(models.Model):
    cpf_estagiario = CPFField(primary_key=True)
    nome_estagiario = models.CharField(max_length=100)
    rg_estagiario = models.CharField(max_length=12)
    turno_estagiario = models.CharField(max_length=10)
    email_estagiario = models.CharField(max_length=200)
    semestre_estagiario = models.IntegerField()
    nis_pis_estagiario = models.CharField(max_length=14)
    telefone_estagiario = models.CharField(max_length=15)
    nome_responsavel_estagiario = models.CharField(max_length=100)
    data_nascimento_estagiario = models.CharField(max_length=10)
    genero_estagiario = models.CharField(max_length=9)
    raca_estagiario = models.CharField(max_length=8)
    bairro_estagiario = models.CharField(max_length=36)
    numero_estagiario = models.CharField(max_length=6)
    complemento_estagiario = models.CharField(max_length=200)
    matricula_estagiario = models.CharField(max_length=8)
    situacao_estagiario = models.CharField(max_length=15)
    #FOREIGN KEY
    supervisor_estagiario = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name="supervisor", null = True)
    sede_estagiario = models.ForeignKey(Sede, on_delete=models.PROTECT, related_name="sede", null = True)
    faculdade_estagiario = models.ForeignKey(Faculdade, on_delete=models.PROTECT, related_name="faculdade", null = True)
    programa_estagiario = models.ForeignKey(Programa, on_delete=models.PROTECT, related_name="programa", null = True)
    edital_estagiario = models.ForeignKey(Edital, on_delete=models.PROTECT, related_name="edital", null = True)
    curso_estagiario = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="curso", null = True)
    
    def __str__(self):
        return self.nome_estagiario

