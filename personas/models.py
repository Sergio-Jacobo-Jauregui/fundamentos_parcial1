from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from ciclos.models import Ciclo
from aulas.models import Aula, Curso

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, help_text="Nombre completo del estudiante.")
    apellido = models.CharField(max_length=50)
    codigo = models.CharField(max_length=8, unique=True, help_text="Codigo del estudiante.")
    carrera = models.CharField(max_length=50, help_text="Carrera universitaria que cursa el estudiante.")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="estudiantes", help_text="Ciclo universitario del estudiante.")
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True, blank=True, related_name="estudiantes", help_text="Aula asignada al estudiante.")
    correo = models.EmailField(unique=True, help_text="Correo electrónico institucional del estudiante.", validators=[EmailValidator()])
    edad = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(99)],
        help_text="Edad del estudiante. Debe estar entre 16 y 99 años."
    )
    fecha_registro = models.DateTimeField(help_text="Fecha en la que se registró el estudiante.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=150, help_text="Nombre completo del estudiante.")
    apellido = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100, help_text="Título académico, por ejemplo, 'Dr.', 'Mtro.', 'Ing.', etc.")
    correo = models.EmailField(unique=True, help_text="Correo electrónico institucional del estudiante.", validators=[EmailValidator()])
    cursos = models.ManyToManyField(Curso, related_name="profesores")
    fecha_registro = models.DateTimeField(help_text="Fecha en la que se registró el estudiante.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
