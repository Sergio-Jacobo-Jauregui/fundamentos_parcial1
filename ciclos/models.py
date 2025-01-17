from django.db import models

class Ciclo(models.Model):
    grado = models.PositiveSmallIntegerField(help_text="Grado del ciclo universitario, por ejemplo, 1")
    fecha_inicio = models.DateField(help_text="Fecha de inicio del ciclo.")
    fecha_fin = models.DateField(help_text="Fecha de fin del ciclo.")
    activo = models.BooleanField(default=True, help_text="Indica si el ciclo está activo.")

    def __str__(self):
        return self.grado
