# Generated by Django 4.0.5 on 2022-06-24 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialties',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic_site.specialty', verbose_name='Напрямки'),
        ),
    ]
