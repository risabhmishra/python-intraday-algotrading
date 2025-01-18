import backtrader as bt


class VWAP(bt.Indicator):
    lines = ("vwap",)
    params = dict(period=14)

    def __init__(self):
        self.addminperiod(self.params.period)
        self.lines.vwap = bt.indicators.SumN(
            self.data.volume * (self.data.high + self.data.low + self.data.close) / 3,
            period=self.params.period,
        ) / bt.indicators.SumN(self.data.volume, period=self.params.period)
