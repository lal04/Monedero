from django.contrib import admin
from .models import (Categoria, Registro, 
                     Estado, Acreedor, Prestamo)  # Importa los modelos necesarios



@admin.register(Registro)  # Registra el modelo 'Registro' en el panel de admin con una clase personalizada
class RegistroAdmin(admin.ModelAdmin):
    
    
    #
    list_display = [field.name for field in Registro._meta.fields] 
    # Muestra estas columnas en la lista del admin de forma automatica, por defecto todas las columnas

    list_filter = ('categoria', 'fecha', 'estado')  
    # Agrega filtros laterales por categoría y por fecha

    search_fields = ('descripcion',)  
    # Permite buscar por el campo 'descripcion' en el buscador superior

    list_display_links = ('descripcion',)  
    # Convierte la columna 'descripcion' en enlace para acceder al detalle del registro

    list_per_page = 25  
    # Define cuántos elementos se muestran por página (paginador)

    list_max_show_all = 200  
    # Límite máximo de ítems si se usa "Mostrar todo"

    show_full_result_count = False  
    # Desactiva el conteo total de resultados para mejorar rendimiento

    actions = None  
    # Elimina la acción por defecto "Eliminar seleccionados" del panel

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'tipo',)
    list_per_page=25
    list_filter=('tipo',)
    search_fields=('nombre','tipo',)
    actions = None

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display=('fecha', 'acreedor', 'tipo','monto')
    list_display_links=('acreedor',)
    list_per_page=25
    list_filter=('acreedor', 'tipo',)
    search_fields=('acreedor','tipo',)
    actions = None
    
#QUITAMOS EL REGISTRO HASTA QUE VUELA A SER NECESARIO###

# @admin.register(Estado)
# class EstadoAdmin(admin.ModelAdmin):
#     list_display=('tipo',)
#     list_per_page=25
#     search_fields=('tipo',)
#     actions = None


