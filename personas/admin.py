from django.contrib import admin
from .models import Estudiante, Profesor

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'aula')

    def nombre_completo(self, obj):
        return str(obj)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo')

    def nombre_completo(self, obj):
        return str(obj)

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor, ProfesorAdmin)
