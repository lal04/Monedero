from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import PagoPrestamo, Persona, Registro,Prestamo
from datetime import timedelta

@receiver(post_save, sender=User)
def autostaff(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True
        instance.save()

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
        if instance.tipo.nombre== 'Ingreso':
        
            Prestamo.objects.create(
                usuario=instance.usuario,
                fecha=instance.fecha,
                fecha_pago=instance.fecha+timedelta(days=30),
                detalle=instance.detalle,
                persona=instance.persona,
                monto=instance.monto,
                
            )
        elif instance.tipo.nombre== 'Gasto':
            PagoPrestamo.objects.create(
                usuario=instance.usuario,
                fecha=instance.fecha,
                detalle=instance.detalle,
                monto=instance.monto,
                persona=instance.persona,
                
            )
@receiver(post_save, sender=Prestamo)
def aumentar_saldo_persona(sender, instance, created, **kwargs):
    
    persona= instance.persona
    
    total_prestamos=Prestamo.objects.filter(persona=instance.persona).aggregate(total=Sum('monto'))['total'] or 0
    
    persona.saldo=total_prestamos
    persona.save()
    
@receiver(post_save, sender=PagoPrestamo)
def disminuir_saldo_persona(sender, instance, created, **kwargs):
    persona= instance.persona         
            
    total_pagos=PagoPrestamo.objects.filter(persona=instance.persona).aggregate(total=Sum('monto'))['total'] or 0
    
    persona.saldo-=total_pagos
    persona.save()
   
            
# @receiver(post_delete, sender=Registro)
# def revertir_saldo_prestamo(sender, instance, **kwargs):
#     if instance.prestamo:
#         instance.prestamo.saldo+=instance.monto
#         instance.prestamo.save()