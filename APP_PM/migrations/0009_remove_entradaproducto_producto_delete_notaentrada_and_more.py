# Generated by Django 5.1.1 on 2024-11-12 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0008_notaentrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradaproducto',
            name='producto',
        ),
        migrations.DeleteModel(
            name='NotaEntrada',
        ),
        migrations.DeleteModel(
            name='EntradaProducto',
        ),
    ]
