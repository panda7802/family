# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
from filer.fields.image import FilerImageField


class ZF(models.Model):
    """
    祝福
    """
    name = models.CharField('姓名', max_length=128, default="", blank=False)  # 图片
    zf = models.CharField('祝福', max_length=128, default="", blank=False)  # 祝福
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.name + " : " + self.zf


class GrowingUp(models.Model):
    """
    成长
    """
    name = models.CharField('名称', max_length=128, default="", blank=True)
    take_time = models.DateTimeField('时间', default=timezone.now)
    # photo = models.FileField('图片', upload_to=MEDIA_ROOT, default="", blank=True)  # 图片
    pic = FilerImageField(related_name='product_image', on_delete=models.CASCADE)
    desc = models.CharField('描述', max_length=1024, default="", blank=True)
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)
    bak_data1 = models.CharField('备用字段1', max_length=1024, default="", blank=True)

    def __unicode__(self):
        return self.name
