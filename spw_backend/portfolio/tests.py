# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.test import TestCase

from .models import Portfolio, PortfolioStockAction
from stocks.models import Stock


class PortfolioTestCase(TestCase):
	def test_test(self):
		self.assertEqual(1, 1)


# Test deleting a portfolio deletes its actions data
class PortfolioDeletionTestCase(TestCase):

	def setUp(self):
		test_stock = Stock(name='Test Stock', ticker='TEST0')
		test_stock.save()
		test_portfolio = Portfolio(name='testportfolio')
		test_portfolio.save()

		for i in xrange(1, 10):
			test_action = PortfolioStockAction(
				buy=True,
				sell=False,
				date=date.today(),
				amount=i,
				value_at_action_time=10.0,
				stock=test_stock
			)
			test_action.save()
			test_portfolio.actions.add(test_action)
			test_portfolio.save()


	def test_portfolio_deletion_deletes_actions(self):
		portfolio_to_delete = Portfolio.objects.get(name='testportfolio')
		portfolio_to_delete.delete()
		self.assertEqual(False, PortfolioStockAction.objects.all().exists())

