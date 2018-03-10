import quandl

from django.core.management.base import BaseCommand


class Command(BaseCommand):

	'''
		Learning how to get data from quandl
		I use this command to try stuff 
	'''

	def handle(self, *args, **options):


		with open('/home/asuka/quandl_api_key') as f:
			quandl.ApiConfig.api_key = f.read().strip()

		data = quandl.get_table(
			'WIKI/PRICES',
			ticker = ['AAPL'],
			qopts = { 'columns': ['ticker', 'date', 'close'] },
			date = { 'gte': '2018-01-01', 'lte': '2018-01-10' }
		)

		# Get Ticker
		print 'TICKER => %s' % str(data.values[0][0])
		print 'DATE => %s' % str(data.values[0][1])
		print 'CLOSE => %s' % str(data.values[0][2])

		# Add values to AAPL (created manually on admin panel)

		print '*'  * 10

