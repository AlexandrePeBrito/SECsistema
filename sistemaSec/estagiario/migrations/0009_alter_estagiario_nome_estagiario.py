# Generated by Django 3.2.11 on 2022-07-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagiario', '0008_auto_20220707_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estagiario',
            name='nome_estagiario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
