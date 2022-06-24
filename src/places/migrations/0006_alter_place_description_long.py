# Generated by Django 4.0.5 on 2022-06-24 11:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_placeimage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Detailed description of the place'),
        ),
    ]