from django.core.management.base import BaseCommand

from stocks.models import Stock
from stocks.utils import fill_stock_history_data


class Command(BaseCommand):

	'''
		CRON [daily]
		
		Gets stock history data that we dont have every day.

		Loops stock.utils.fill_stock_history_data for every stock
		that we have on the database
	'''

	def handle(self, *args, **oprions):

		for s in Stock.objects.all():
			fill_stock_history_data(s.ticker)

		print 'getLatestStockHistoryData END'

