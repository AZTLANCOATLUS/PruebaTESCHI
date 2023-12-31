# Generated by Django 3.2.4 on 2023-09-27 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_alumno_fk_genero'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='alumno',
            table='Alumno_has_genero',
        ),
        migrations.CreateModel(
            name='Alumno_has_genero',
            fields=[
                ('idalumno_has_genero', models.AutoField(db_column='idAlumno_has_genero', primary_key=True, serialize=False)),
                ('fk_genero', models.ForeignKey(db_column='fk_genero', on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
            ],
        ),
    ]
