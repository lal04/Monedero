from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Estado(models.Model):
    
    ESTADOS_CHOICES=(
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
        #('Anulado', 'Anulado'),
    )
    
    tipo=models.CharField(max_length=10, choices=ESTADOS_CHOICES, unique=True)
    
    def __str__(self):
        return self.tipo


class Categoria(models.Model):
    TIPO_CHOICES = (
        ('Ingreso', 'Ingreso'),
        ('Gasto', 'Gasto'),
    )
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=100, unique=True)
    tipo=models.CharField(max_length=10, choices=TIPO_CHOICES, default='Gasto')

    def __str__(self):
        return self.nombre
    
class Tipo(models.Model):
    nombre=models.CharField(max_length=10, help_text='Tipo de movimiento')
    def __str__(self):
        return self.nombre


    
class Persona(models.Model):
    usuario=models.ForeignKey( User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100, unique=True)
    saldo=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True)
    

    def __str__(self):
        return self.nombre
    
    
class Prestamo(models.Model):
    
    usuario=models.ForeignKey( User, on_delete=models.CASCADE)
    fecha=models.DateField()
    fecha_pago=models.DateField(null=True, blank=True)
    detalle=models.CharField(max_length=200)
    persona=models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    monto=models.DecimalField(max_digits=10, decimal_places=2)
    saldo=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    
    def clean(self):
        if self.fecha >= self.fecha_pago:
            raise ValidationError('La fecha de pago debe ser posterior a la fecha del prestamo')
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.saldo=self.monto
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f'{self.persona} - {self.monto}'


class Registro(models.Model):
    PRESTAMO_CHOICES = (
        (True, 'Si'),
        (False, 'No'),
    )
    usuario=models.ForeignKey( User, on_delete=models.CASCADE)    
    fecha=models.DateField(help_text='Fecha del movimiento')
    tipo=models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True, blank=True) 
    detalle=models.CharField(max_length=200, help_text='Descripción del movimiento', db_column='descripcion')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    monto=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.ForeignKey(Estado, on_delete=models.CASCADE, default=2)
    prestamo=models.BooleanField(default=False,help_text='¿Es un prestamo?', choices=PRESTAMO_CHOICES)
    persona=models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.detalle} - {self.monto}"