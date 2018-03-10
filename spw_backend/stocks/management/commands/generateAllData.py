from dateutil.relativedelta import relativedelta

from django.db.utils import OperationalError
from django.utils import timezone
from django.core.management.base import BaseCommand

from stocks.models import Stock, StockHistory
from stocks.utils import generate_stock_history_data



class Command(BaseCommand):

	'''
		Loops all stocks on the database and generates stockHistory
		data for 5 years. (date and close price)
	'''

	def handle(self, *args, **oprions):

		# Dates
		today = timezone.now()
		five_years_ago = today - relativedelta(years=5)

		today_str = today.strftime('%Y-%m-%d')
		five_years_ago_str = five_years_ago.strftime('%Y-%m-%d')

		# Loop all stocks
		for s in Stock.objects.all():

			print 'Generating 5 years of data for %s' % s.ticker

			# Get all time data and save it in database
			data = generate_stock_history_data(s.ticker, five_years_ago, today)
			for d in data.values:

				# Preventas a warning
				hdate = timezone.make_aware(
					d[1].to_pydatetime(),
					timezone.get_current_timezone()
				)

				StockHistory.objects.create(
					ticker=d[0],
					close= d[2],
					date= hdate
				)

		print 'generateAllData END'

