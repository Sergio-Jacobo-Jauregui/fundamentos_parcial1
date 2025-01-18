from django.db import models
from datetime import datetime, timedelta
from django.dispatch import receiver
from ciclos.models import Ciclo
from django.core.validators import MinValueValidator, MaxValueValidator

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
    hora_inicio = models.TimeField(max_length=100, help_text="Hora de inicio de este curso")
    duracion = models.DecimalField(max_digits=3, decimal_places=1, help_text="Duración del curso en horas", validators=[MinValueValidator(0), MaxValueValidator(7)])
    hora_fin = models.TimeField(max_length=100, help_text="Hora de fin de este curso")

    def __str__(self):
        return f"Curso: {self.curso.nombre}, Aula: {self.aula.nombre}"

    def save(self, *args, **kwargs):
        print(2222)
        hora_inicio_raw = datetime.strptime(self.hora_inicio, "%H:%M:%S").time()
        hora_inicio_dt = datetime.combine(datetime.today(), hora_inicio_raw)

        horas_a_agregar = timedelta(hours=self.duracion)
        nueva_hora = hora_inicio_dt + horas_a_agregar
        self.hora_fin = nueva_hora.time()

        super().save(*args, **kwargs)
