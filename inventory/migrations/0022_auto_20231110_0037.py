# Generated by Django 3.0.7 on 2023-11-09 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_stock_square_metre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='square_metre',
        ),
        migrations.AddField(
            model_name='stock',
            name='square_meter',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]