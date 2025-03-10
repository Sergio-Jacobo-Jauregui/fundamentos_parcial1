# Generated by Django 5.1.5 on 2025-01-17 22:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursoaula',
            name='fecha_asignacion',
        ),
        migrations.RemoveField(
            model_name='cursoaula',
            name='horario',
        ),
        migrations.AddField(
            model_name='cursoaula',
            name='hora_fin',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Hora de fin de este curso', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cursoaula',
            name='hora_inicio',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Hora de inicio de este curso', max_length=100),
            preserve_default=False,
        ),
    ]
