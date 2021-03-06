# Generated by Django 4.0.5 on 2022-06-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=32, verbose_name='Title')),
                ('description_short', models.CharField(blank=True, max_length=250, null=True, verbose_name='Short description of the place')),
                ('description_long', models.TextField(blank=True, null=True, verbose_name='Detailed description of the place')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
    ]
