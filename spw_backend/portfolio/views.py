# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pprint import pprint

from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse, Http404

from .models import Portfolio, PortfolioStockAction
from stocks.models import StockHistory


def GetAllPortfolioStockData(request, portfolio_name):
	"""
		Gets all stock data related to portfolio.
		
		For example if this portfolio bought FB in 2018-03-07, we return:

		data = {
			'FB' : [
				{'close':12.0, 'date':2018-03-07}
				...
			]
		}
	"""

	data = {}
	portfolio = Portfolio.objects.get(name=portfolio_name)

	for action in portfolio.actions.filter(buy=True):

		# All the dates
		stock_history = StockHistory.objects.filter(
			ticker=action.stock.ticker,
			date__gte=action.date
		)

		data[action.stock.ticker] = [
			{'close':x.close, 'date':x.date} for x in stock_history 
		] 

	return JsonResponse(data, safe=False)

