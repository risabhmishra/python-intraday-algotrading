from pprint import pprint

from data import fetch_history

symbol = "ADANIGREEN.NS"

history = fetch_history.fetch_stock_data(symbol)
backtest_data = fetch_history.cleanup_data(history)
pprint(backtest_data.head())