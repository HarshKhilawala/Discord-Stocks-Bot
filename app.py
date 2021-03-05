import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import plotly.express as px
import os
# import bot

data_df = yf.download('TCS',period="1d",interval="1d",progress=False)
data_df.head()

# ticker = yf.Ticker('TCS')
# data_df = ticker.history(period="1d", interval="1d") # Possible parameters period, interval etc..
# tcs_df['Close'].plot(title="TCS's Stock Price")

fig = px.line(data_df,y='Close',title='TCS Share Price Over time')
# fig.show()

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")

# Allow date as column  # VERY IMPORTANT
data_df.reset_index(inplace=True)

stock_data = {
    'date': data_df['Date'][0].date(),
    'open': data_df['Open'][0],
    'high': data_df['High'][0],
    'low': data_df['Low'][0],
    'close': data_df['Close'][0],
    'adjclose': data_df['Adj Close'][0],
    'volume': data_df['Volume'][0]
}


if __name__ == "__main__":
    print(stock_data)
