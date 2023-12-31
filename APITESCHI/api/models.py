from django.db import models


# Create your models here.
class Genero (models.Model):
        idGenero= models.AutoField(primary_key=True, db_column='idGenero')
        tipo_genero= models.TextField(db_column='tipo_genero')
        class Meta:
         db_table='Generos'
         
         
class Alumno (models.Model):
    idAlumno = models.IntegerField(primary_key=True, db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100, db_column='nameAlumno')
    class Meta:
        db_table='Alumnos'
        
class Alumno_has_genero  (models.Model):
    idalumno_has_genero = models.AutoField(primary_key=True, db_column='idAlumno_has_genero')
    fk_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE, db_column='fk_alumno')
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='fk_genero')
    class Meta:
          db_table='Alumno_has_genero'

        
        
