import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

import yfinance as yf


def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    # get all stock info
    print(stock.info)

    # get historical market data
    hist = stock.history(period="1y")
    pprint(hist.head())
    return hist


def cleanup_data(data):
    # Check for missing values
    print(data.isnull().sum())

    # Clean data (if required)
    data_cleaned = data[['Close', 'Open', 'High', 'Low', 'Volume']]

    # Ensure 'Date' is the index
    data.index = pd.to_datetime(data.index)

    # Select only required columns and rename them for Backtrader
    backtest_data = data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    # Preview the final data
    print(backtest_data.head())

    return backtest_data


def plot_data(data, symbol):
    # Plot the closing prices
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label=f"{symbol} Closing Price")
    plt.title(f"{symbol} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()
