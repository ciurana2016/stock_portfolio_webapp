import quandl

from dateutil.relativedelta import relativedelta

from django.utils import timezone

from .models import Stock, StockHistory


'''
	Conects to Quandl and gets the stock data from the ticker
	and dates selected
'''
def generate_stock_history_data(ticker, from_date, to_date):

	# Quandl login
	with open('/home/asuka/quandl_api_key') as f:
		quandl.ApiConfig.api_key = f.read().strip()

	# Retrieve data
	data = quandl.get_table(
		'WIKI/PRICES',
		ticker = [ticker],
		qopts = { 'columns': ['ticker', 'date', 'close'] },
		date = { 'gte': from_date, 'lte': to_date }
	)

	return data


'''
	Looks at the last day of data saved for a stock
	and fills the stockHistory data from that day to today
	[TODO not-tested]
'''
def fill_stock_history_data(ticker):

	today = timezone.now()
	last_stock_history = StockHistory.objects.filter(ticker=ticker).latest('date')
	last_db_change = last_stock_history.date + relativedelta(days=1)

	if today > last_db_change:

		today_str = today.strftime('%Y-%m-%d')
		last_day_str = last_db_change.strftime('%Y-%m-%d')
		data = generate_stock_history_data(ticker, last_day_str, today_str)

		try:
			# Preventas a warning
			hdate = timezone.make_aware(
				data.values[0][1].to_pydatetime(),
				timezone.get_current_timezone()
			)
		
			StockHistory.objects.create(
				ticker=data.values[0][0],
				close= data.values[0][2],
				date= hdate
			)

		except IndexError:
			pass


	


