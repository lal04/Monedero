from django.contrib import admin
from django.db.models import Q
from .models import (Categoria, Registro, 
                     Estado, Acreedor, Prestamo)  # Importa los modelos necesarios



@admin.register(Registro)  # Registra el modelo 'Registro' en el panel de admin con una clase personalizada
class RegistroAdmin(admin.ModelAdmin):
    
    exclude=['usuario']
    
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
    
    def get_queryset(self, request):
        qs= super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(usuario=request.user)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuario= request.user
        return super().save_model(request, obj, form, change)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    exclude=['usuario']
    list_display=('nombre', 'tipo',)
    list_per_page=25
    list_filter=('tipo',)
    search_fields=('nombre','tipo',)
    actions = None
    
    def get_queryset(self, request):
        qs= super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(usuario=request.user) | Q(usuario__isnull=True))
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuario= request.user
        return super().save_model(request, obj, form, change)
        

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    exclude=['usuario']
    list_display=('fecha', 'detalle','acreedor', 'tipo','monto', 'saldo')
    list_display_links=('detalle',)
    list_per_page=25
    list_filter=('acreedor', 'tipo',)
    search_fields=('acreedor','tipo',)
    actions = None
    
    def get_queryset(self, request):
        qs= super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(usuario=request.user)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuario= request.user
        return super().save_model(request, obj, form, change)
    
#QUITAMOS EL REGISTRO HASTA QUE VUELA A SER NECESARIO###

# @admin.register(Estado)
# class EstadoAdmin(admin.ModelAdmin):
#     list_display=('tipo',)
#     list_per_page=25
#     search_fields=('tipo',)
#     actions = None


