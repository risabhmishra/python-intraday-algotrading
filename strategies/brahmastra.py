import backtrader as bt
from indicators.supertrend import SuperTrend
from indicators.vwap import VWAP


class BrahmastraStrategy(bt.Strategy):
    stop_loss = None
    take_profit = None

    def __init__(self):
        self.supertrend = SuperTrend(self.data)
        self.macd = bt.indicators.MACD(self.data)
        self.vwap = VWAP(self.data)
        # Logic to enter a trade based on all conditions
        self.buy_signal = None
        self.sell_signal = None

    def next(self):
        if self.macd.macd[0] > self.macd.signal[0] and self.vwap[0] < self.data.close[0] < self.supertrend[0]:
            self.buy_signal = True
            self.sell_signal = False
        elif self.macd.macd[0] < self.macd.signal[0] and self.vwap[0] > self.data.close[0] > self.supertrend[0]:
            self.buy_signal = False
            self.sell_signal = True

        if self.buy_signal:
            self.stop_loss = self.data.close[0] - (self.supertrend[0] * 0.01)
            self.take_profit = self.data.close[0] + (self.supertrend[0] * 0.03)
            self.buy()

        if self.sell_signal:
            self.stop_loss = self.data.close[0] + (self.supertrend[0] * 0.01)
            self.take_profit = self.data.close[0] - (self.supertrend[0] * 0.03)
            self.sell()

        if self.position:  # If in position, check for stop loss/take profit
            if self.data.close[0] <= self.stop_loss or self.data.close[0] >= self.take_profit:
                self.close()
