from django.db import models


class Specialist(models.Model):

    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"

    name = models.CharField('Назва', max_length=160)
    slug = models.SlugField(max_length=160, unique=True)
    specialties = models.ManyToManyField('Specialty', verbose_name='Напрямки', null=True)
    description = models.TextField('Опис')
    date_birth = models.DateField('Дата народження')
    work_experience = models.IntegerField('Досвід роботи')
    number_of_sort = models.BigIntegerField('Номер сортування')

    def __str__(self):
        return self.name


class Specialty(models.Model):

    class Meta:
        verbose_name = "Напрямок"
        verbose_name_plural = "Напрямки"

    name = models.CharField('Назва', max_length=160)
    slug = models.SlugField(max_length=160, unique=True)
    number_of_sort = models.BigIntegerField('Номер сортування')

    def __str__(self):
        return self.name

