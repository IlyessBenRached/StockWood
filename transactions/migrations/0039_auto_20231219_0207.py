# Generated by Django 3.0.7 on 2023-12-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0038_auto_20231219_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeritem',
            name='total_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
