from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registro,Prestamo

@receiver(post_save, sender=Registro)
def acualizar_saldo_prestamo(sender, instance, created , **kwargs):
    if created and instance.prestamo:
        if instance.categoria.nombre == 'Amortizacion':
            instance.prestamo.saldo-=instance.monto
            instance.prestamo.save()