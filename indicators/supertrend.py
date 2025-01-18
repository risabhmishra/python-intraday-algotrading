import backtrader as bt

class SuperTrend(bt.Indicator):
    params = (
        ('period', 20),
        ('multiplier', 2),
    )
    lines = ('supertrend',)
    plotinfo = dict(subplot=False)

    def __init__(self):
        atr = bt.indicators.ATR(self.data, period=self.params.period)
        hl2 = (self.data.high + self.data.low) / 2
        self.lines.supertrend = bt.If(
            self.data.close > hl2 + self.params.multiplier * atr,
            hl2 + self.params.multiplier * atr,
            hl2 - self.params.multiplier * atr
        )
