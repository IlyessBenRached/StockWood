# Generated by Django 3.0.7 on 2023-12-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0045_auto_20231219_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='perprice',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='totalprice',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=30),
        ),
    ]
