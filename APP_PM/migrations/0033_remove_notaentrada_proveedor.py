# Generated by Django 5.1.3 on 2024-12-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0032_remove_notaentrada_cliente_notaentrada_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notaentrada',
            name='proveedor',
        ),
    ]
