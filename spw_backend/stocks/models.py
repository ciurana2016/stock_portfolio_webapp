# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StockHistory(models.Model):

	ticker = models.CharField(max_length=10)
	close = models.FloatField(default=0.0)
	date = models.DateTimeField()

	def __unicode__(self):
		return '%s, Close: %s, Date: %s' % (self.ticker, self.close, self.date)


class Stock(models.Model):
	
	name = models.CharField(max_length=100)
	ticker = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name

	def delete(self):
		# Deletes all stockHistory for that ticker
		for stock_history in StockHistory.objects.filter(ticker= self.ticker):
			stock_history.delete()

		super(Stock, self).delete()
