from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Registro,Prestamo
@receiver(pre_save, sender=Registro)
def guardar_datos_anteriores(sender, instance, **kwargs):
    if instance.pk:
        old = Registro.objects.get(pk=instance.pk)
        instance._old_monto = old.monto
        instance._old_prestamo = old.prestamo
        instance._old_categoria = old.categoria
        

@receiver(post_save, sender=Registro)
def acualizar_saldo_prestamo(sender, instance, created , **kwargs):
    if created and instance.prestamo:
        if instance.categoria.nombre == 'Amortizacion':
            instance.prestamo.saldo-=instance.monto
            instance.prestamo.save()
    elif not created:
        # Recuperar datos anteriores (definidos en pre_save)
        old_prestamo = getattr(instance, '_old_prestamo', None)
        old_monto = getattr(instance, '_old_monto', None)
        old_categoria = getattr(instance, '_old_categoria', None)
        nueva_categoria = instance.categoria.nombre
        nuevo_prestamo = instance.prestamo
        nuevo_monto = instance.monto
        

        # Si antes era amortización y tenía préstamo → revertimos ese cambio
        if old_categoria and old_categoria.nombre == 'Amortizacion' and old_prestamo:
            
            old_prestamo.saldo += old_monto
            print(old_prestamo.saldo)
            old_prestamo.save()

        # Si ahora es amortización y tiene préstamo → aplicamos nuevo descuento
        if nueva_categoria == 'Amortizacion' and nuevo_prestamo:
            nuevo_prestamo.saldo -= nuevo_monto
            nuevo_prestamo.save()
            
@receiver(post_delete, sender=Registro)
def revertir_saldo_prestamo(sender, instance, **kwargs):
    if instance.prestamo and instance.categoria.nombre == 'Amortizacion':
        instance.prestamo.saldo+=instance.monto
        instance.prestamo.save()