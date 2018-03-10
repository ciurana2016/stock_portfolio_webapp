# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

from .utils import generate_stock_history_data
from .models import Stock, StockHistory


class StockTestCase(TestCase):

	def setUp(self):
		# Test deleting a stock deletes its history data
		Stock.objects.create(name='Test Stock', ticker='TEST0')
		for i in xrange(1, 10):
			StockHistory.objects.create(
				ticker = 'TEST0',
				close = 2*i,
				date = timezone.now()
			)

	def test_generate_stock_history_data(self):
		d = generate_stock_history_data('AAPL', '2017-01-03', '2017-01-03')
		self.assertEqual(d.values[0][0], u'AAPL')
		self.assertEqual(d.values[0][2], 116.15)

	def test_stock_deletion_deletes_history(self):
		stock_to_delete = Stock.objects.get(ticker='TEST0')
		stock_to_delete.delete()
		self.assertEqual(False, StockHistory.objects.filter(ticker='TEST0').exists())