# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Inquire(models.Model):
    time = models.DateTimeField(verbose_name='时间')
    key = models.CharField(max_length=128, verbose_name='关键字')



class Esconfig(models.Model):
    ip = models.CharField(max_length=128, verbose_name='IP')
    port = models.CharField(max_length=128, verbose_name='端口')
    user = models.CharField(max_length=128, verbose_name='用户', default='')
    password = models.CharField(max_length=128, verbose_name='密码', default='')
    indexname = models.CharField(max_length=128, verbose_name='索引')

