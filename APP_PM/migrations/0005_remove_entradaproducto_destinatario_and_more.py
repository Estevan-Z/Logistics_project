# Generated by Django 5.1.1 on 2024-09-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0004_entradaeliminada_entradaproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradaproducto',
            name='destinatario',
        ),
        migrations.RemoveField(
            model_name='entradaproducto',
            name='retiro',
        ),
    ]
