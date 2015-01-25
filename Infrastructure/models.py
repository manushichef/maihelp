#-*- coding: utf-8 -*-
from django.db import models

class Department(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер кафедры')
    name = models.CharField(max_length=150, verbose_name='Название кафедры')
    faculty = models.IntegerField(max_length=5, verbose_name='Факультет')
    chief = models.CharField(max_length=150, verbose_name='Заведущюий кафедрой')
    date_open = models.DateField(verbose_name='Дата открытия')
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(max_length=150, verbose_name='Телефоны кафедры')
    site = models.CharField(max_length=50, verbose_name='Сайт кафедры')
    email = models.EmailField(verbose_name='Электронная почта')
    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'кафедры'
        def __unicode__(self):
            return self.number + ' ' + self.name



