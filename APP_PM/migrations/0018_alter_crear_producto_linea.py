# Generated by Django 5.1.1 on 2024-11-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_PM', '0017_crear_producto_linea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crear_producto',
            name='linea',
            field=models.CharField(choices=[('insecticidas', 'Insecticidas'), ('fertilizantes', 'Fertilizantes'), ('materia prima', 'Materia Prima'), ('insumos', 'Insumos'), ('coayudantes', 'Coayudantes'), ('gravados', 'Gravados'), ('bioinsumos', 'Bioinsumos'), ('fungicidas', 'Fungicidas'), ('maquila', 'Maquila'), ('herbicidas', 'Herbicidas')], max_length=100),
        ),
    ]
