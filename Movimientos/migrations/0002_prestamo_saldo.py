# Generated by Django 4.2 on 2025-04-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movimientos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
