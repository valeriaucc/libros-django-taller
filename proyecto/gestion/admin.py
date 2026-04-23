from django.contrib import admin

from proyecto.gestion.models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
 list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
 list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
 list_filter = ('autor', 'genero', 'fecha_publicacion')
