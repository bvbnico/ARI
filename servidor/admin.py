from django.contrib import admin

# Register your models here.

from .models import estaciones, clientes, sensores, tipo_sensor, usuarios

admin.site.register(estaciones)
admin.site.register(clientes)
admin.site.register(sensores)
admin.site.register(tipo_sensor)
admin.site.register(usuarios)

"""# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)"""
