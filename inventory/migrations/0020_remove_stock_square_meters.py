# Generated by Django 3.0.7 on 2023-11-09 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_stock_square_meters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='square_meters',
        ),
    ]
