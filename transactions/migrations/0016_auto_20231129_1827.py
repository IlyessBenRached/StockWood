# Generated by Django 3.0.7 on 2023-11-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_auto_20231129_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdetails',
            name='cgst',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='offerdetails',
            name='igst',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='offerdetails',
            name='total',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]