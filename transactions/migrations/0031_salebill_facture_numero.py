# Generated by Django 3.0.7 on 2023-12-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0030_remove_salebill_facture_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='salebill',
            name='facture_numero',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
