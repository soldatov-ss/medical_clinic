# Generated by Django 4.0.5 on 2022-06-25 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_site', '0003_remove_specialist_specialties_specialist_specialties'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specialist',
            new_name='Doctor',
        ),
    ]
