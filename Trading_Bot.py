import pandas as pd
import numpy as np
from time import sleep
import yfinance as yf

#Set-up your screener-Filter parameters to find tradable stocks
#Review min price based on tradable peny stocks volatility and change
min_price = 0.1
max_price = 5
min_volume = 750000

# Sectors to exclude
excluded_sectors = ['Finance', 'Government', 'Miscellaneous', 'Utilities']

# Download Market data every 5 sec
while True:
    #NYSE & Nasdac Data download
    tickers = yf.Tickers('NYSE, NASDAQ')
    stock_data = tickers.ticker.apply(lambda x: yf.Ticker(x).info)
    order_book_data = tickers.ticker.apply(lambda x: yf.Ticker(x).orderbook)

    #Filter downloaded data based on parameters given
    filtered_data = stock_data[(stock_data['regularMarketPrice'] >= min_price) &
                           (stock_data['regularMarketPrice'] <= max_price) & 
                           (stock_data['regularMarketVolume'] >= min_volume)]

    # Add the order book filter
    filtered_data = filtered_data[['bidSize'].sum() / ['askSize'].sum()] >= 1.5
    
    # Add the market sector filter
    filtered_data = filtered_data[~filtered_data['sector'].isin(excluded_sectors)]


    # Sleep for 5 seconds before updating the data again
    sleep(5)





#Plot stock data ???

#Link bot to trading account 