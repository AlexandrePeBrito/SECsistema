"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField
from ..supervisor.models import Supervisor
from ..estagio.models import Estagio
from ..faculdade.models import Faculdade
from ..sede.models import Sede

class Estagiario(models.Model):
    cpf_estagiario = CPFField(primary_key=True)
    nome_estagiario = models.CharField(max_length=100)
    rg_estagiario = models.CharField(max_length=11)
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
    estagio_estagiario = models.ForeignKey(Estagio, on_delete=models.PROTECT, related_name="estagio", null = True)
    
    def __str__(self):
        return self.nome_estagiario

