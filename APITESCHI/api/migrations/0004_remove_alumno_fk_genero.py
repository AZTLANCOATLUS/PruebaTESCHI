# Generated by Django 3.2.4 on 2023-09-27 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alumno_fk_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fk_genero',
        ),
    ]
