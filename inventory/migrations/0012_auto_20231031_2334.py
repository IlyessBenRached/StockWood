# Generated by Django 3.0.7 on 2023-10-31 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20231031_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='contonaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Contonaire'),
        ),
    ]