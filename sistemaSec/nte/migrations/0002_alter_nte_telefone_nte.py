# Generated by Django 3.2.11 on 2022-07-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nte',
            name='telefone_NTE',
            field=models.CharField(max_length=15),
        ),
    ]
