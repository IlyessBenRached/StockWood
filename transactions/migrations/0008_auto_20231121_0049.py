# Generated by Django 3.0.7 on 2023-11-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_salebill_sale_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salebill',
            name='sale_type',
            field=models.CharField(choices=[('quantity', 'Quantity'), ('cubic_meter', 'Cubic Meter')], default='Null', max_length=20),
        ),
    ]
