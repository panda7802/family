# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from love.models import ZF


class UnderwriterZF(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'name', 'zf')
    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'name')


admin.site.register(ZF, UnderwriterZF)
