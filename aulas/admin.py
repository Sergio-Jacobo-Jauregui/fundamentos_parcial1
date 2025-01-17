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

admin.site.register(Aula, AulaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(CursoAula)