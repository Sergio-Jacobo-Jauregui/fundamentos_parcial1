from django.contrib import admin
from .models import Aula, Curso, CursoAula

class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'capacidad')

    def nombre_completo(self, obj):
        return str(obj)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo')

    def nombre_completo(self, obj):
        return str(obj)

class CursoAulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'dia_completo', 'hora_completo')
    fields = ('curso', 'aula', 'hora_inicio', 'duracion', 'dia')

    def nombre_completo(self, obj):
        return str(obj)

    def dia_completo(self, obj):
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        return f"{str(obj.dia)}: {dias[obj.dia - 1]}"

    def hora_completo(self, obj):
        return f"{str(obj.hora_inicio)} - {obj.hora_fin}"

admin.site.register(Aula, AulaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(CursoAula, CursoAulaAdmin)