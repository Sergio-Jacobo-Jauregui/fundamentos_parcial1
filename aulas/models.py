from django.db import models
from ciclos.models import Ciclo

class Aula(models.Model):
    nombre = models.CharField(max_length=2, help_text="Letra del aula.")
    capacidad = models.PositiveIntegerField(help_text="Capacidad máxima de estudiantes en el aula.")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="aulas", help_text="Ciclo al que pertenece esta aula.")

    def __str__(self):
        return f"Ciclo {self.ciclo}: {self.nombre}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del curso, por ejemplo, 'Matemáticas Avanzadas'.")
    descripcion = models.TextField(blank=True, help_text="Descripción del curso.")
    creditos = models.PositiveSmallIntegerField(help_text="Número de créditos del curso.")
    fecha_creacion = models.DateTimeField(auto_now_add=True, help_text="Fecha en la que se creó el curso.")

    def __str__(self):
        return self.nombre

class CursoAula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="curso_aulas")
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name="curso_aulas")
    horario = models.CharField(max_length=100, help_text="Horario del curso en el aula, por ejemplo, 'Lunes 8:00-10:00'.")
    fecha_asignacion = models.DateTimeField(auto_now_add=True, help_text="Fecha en la que se asignó el curso al aula.")

    def __str__(self):
        return f"Curso: {self.curso.nombre}, Aula: {self.aula.nombre}, Horario: {self.horario}"