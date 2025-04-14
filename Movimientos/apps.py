from django.apps import AppConfig


class MovimientosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Movimientos'
    
    def ready(self):
        import Movimientos.signals