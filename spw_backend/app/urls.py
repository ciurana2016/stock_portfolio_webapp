# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib import admin

from portfolio.views import GetAllPortfolioStockData

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Portfolio
    url(r'^get_all_portfolio_stock_data/(?P<portfolio_name>[\w\d\ \.]+)/$', GetAllPortfolioStockData)

]
