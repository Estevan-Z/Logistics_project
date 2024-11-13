# Generated by Django 5.1.1 on 2024-11-12 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0009_remove_entradaproducto_producto_delete_notaentrada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP_PM.crear_producto')),
            ],
        ),
    ]
