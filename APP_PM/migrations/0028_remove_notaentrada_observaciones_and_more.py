# Generated by Django 5.1.3 on 2024-11-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0027_alter_crear_producto_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notaentrada',
            name='observaciones',
        ),
        migrations.AddField(
            model_name='notaentrada',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notaentrada',
            name='lote',
            field=models.CharField(default='SIN_LOTE', max_length=100),
        ),
    ]