# Generated by Django 4.2 on 2025-04-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movimientos', '0011_tipo_alter_persona_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='prestamo',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False, help_text='¿Es un prestamo?'),
        ),
    ]
