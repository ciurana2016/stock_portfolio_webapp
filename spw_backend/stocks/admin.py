# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Stock, StockHistory


admin.site.register(Stock)
admin.site.register(StockHistory)