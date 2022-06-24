# Generated by Django 4.0.5 on 2022-06-24 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('number_of_sort', models.BigIntegerField(verbose_name='Номер сортування')),
            ],
            options={
                'verbose_name': 'Напрямок',
                'verbose_name_plural': 'Напрямки',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=160, unique=True)),
                ('description', models.CharField(max_length=250, verbose_name='Опис')),
                ('date_birth', models.DateField(verbose_name='Дата народження')),
                ('work_experience', models.IntegerField(verbose_name='Досвід роботи')),
                ('number_of_sort', models.BigIntegerField(verbose_name='Номер сортування')),
                ('specialties', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic_site.specialty')),
            ],
            options={
                'verbose_name': 'Лікар',
                'verbose_name_plural': 'Лікарі',
            },
        ),
    ]