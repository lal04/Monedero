from django.db import models

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
    nombre=models.CharField(max_length=100, unique=True)
    tipo=models.CharField(max_length=10, choices=TIPO_CHOICES, default='Gasto')

    def __str__(self):
        return self.nombre



class Registro(models.Model):
    
    fecha=models.DateField(auto_now=True)    
    descripcion=models.CharField(max_length=200)
    categoria=models.ForeignKey('Categoria', on_delete=models.CASCADE)
    monto=models.DecimalField(max_digits=10, decimal_places=2)
    # Relación con el modelo Estado, por defecto 'Pendiente'
    estado=models.ForeignKey('Estado', on_delete=models.CASCADE, null=True, default=2)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
