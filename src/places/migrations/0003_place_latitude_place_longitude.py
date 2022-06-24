# Generated by Django 4.0.5 on 2022-06-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name="Latitude of the place's location"),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name="Longitude of the place's location"),
        ),
    ]