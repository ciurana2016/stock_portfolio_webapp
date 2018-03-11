# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from stocks.models import Stock


class PortfolioStockAction(models.Model):

	buy = models.BooleanField()
	sell = models.BooleanField()
	action_execution_time = models.DateField(auto_now=True)
	date = models.DateTimeField()
	amount = models.IntegerField()
	value_at_action_time = models.FloatField(default=0.0)
	currency = models.CharField(max_length=10, default='USD')
	stock = models.ForeignKey(Stock)


class Portfolio(models.Model):

	name = models.CharField(max_length=100)
	stocks = models.ManyToManyField(Stock, blank=True)
	actions = models.ManyToManyField(PortfolioStockAction, blank=True)

	def __unicode__(self):
		return 'Portfolio: %s' % self.name

	def delete(self):
		# Delete all PortfolioStockActions related
		for action in self.actions.all():
			action.delete()

		super(Portfolio, self).delete()
