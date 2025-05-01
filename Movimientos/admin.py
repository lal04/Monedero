from django.contrib import admin
from django.db.models import Q
from .models import (Categoria, Registro,Tipo, 
                     Estado, Persona, Prestamo,
                     PagoPrestamo)  # Importa los modelos necesarios

#admin.site.register(Tipo)  # Registra el modelo 'Tipo' en el panel de admin
#admin.site.register(Persona)  # Registra el modelo 'Persona' en el panel de admin
#admin.site.register(PagoPrestamo)  # Registra el modelo 'Estado' en el panel de admin
@admin.register(PagoPrestamo)
class PagoPrestamoAdmin(admin.ModelAdmin):
    exclude=['usuario']
    list_display=('fecha','detalle','monto','persona',)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.usuario= request.user
        return super().save_model(request, obj, form, change)
    
    
    
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    exclude=['usuario']
    list_display=('nombre','saldo',)
    list_per_page=25
    search_fields=('nombre',)
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



@admin.register(Registro)  # Registra el modelo 'Registro' en el panel de admin con una clase personalizada
class RegistroAdmin(admin.ModelAdmin):
    
    exclude=['usuario']
    

    list_display = ['fecha','tipo','detalle','categoria','monto','estado',] 
    # Muestra estas columnas en la lista del admin de forma automatica, por defecto todas las columnas

    list_filter = ('categoria', 'fecha', 'estado')  
    # Agrega filtros laterales por categoría y por fecha

    search_fields = ('detalle',)  
    # Permite buscar por el campo 'descripcion' en el buscador superior

    list_display_links = ('detalle',)  
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
    list_display=('fecha', 'fecha_pago','detalle','persona','monto',)
    list_display_links=('detalle',)
    list_per_page=25
    list_filter=('persona',)
    search_fields=('persona',)
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


