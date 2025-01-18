import backtrader as bt

# Load the prepared historical data
from data import fetch_history
from strategies.brahmastra import BrahmastraStrategy

symbol = "ADANIGREEN.NS"

history = fetch_history.fetch_stock_data(symbol)
backtest_data = fetch_history.cleanup_data(history)


# Define a custom data feed for Backtrader
class PandasData(bt.feeds.PandasData):
    params = (
        ("datetime", None),
        ("open", "Open"),
        ("high", "High"),
        ("low", "Low"),
        ("close", "Close"),
        ("volume", "Volume"),
        ("openinterest", -1),
    )


# Load the data into Backtrader
data_feed = PandasData(dataname=backtest_data)

# Create a Backtrader Cerebro engine
cerebro = bt.Cerebro()

# Add the data feed to Cerebro
cerebro.adddata(data_feed)

# Add the Brahmastra strategy to Cerebro
cerebro.addstrategy(BrahmastraStrategy)

# Set the initial capital for the backtesting
cerebro.broker.setcash(100000)  # ₹1,00,000
# cerebro.broker.set_commission(commission=0.001)  # Set commission
# cerebro.addsizer(bt.sizers.FixedSize, stake=10)  # Set the size of each trade

# Run the backtest
print(f"Starting Portfolio Value: {cerebro.broker.getvalue():.2f}")
cerebro.run()
print(f"Final Portfolio Value: {cerebro.broker.getvalue():.2f}")

# Plot the results
cerebro.plot()
