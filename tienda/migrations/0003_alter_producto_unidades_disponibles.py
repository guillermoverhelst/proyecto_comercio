# Generated by Django 4.0.5 on 2023-03-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='unidades_disponibles',
            field=models.FloatField(),
        ),
    ]
