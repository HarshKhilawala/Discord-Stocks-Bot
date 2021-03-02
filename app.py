import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import plotly.express as px
import os

tcs_df = yf.download('TCS',start='2021-01-01',end='2021-01-31',progress=False)
tcs_df.head()

ticker = yf.Ticker('TCS')
tcs_df = ticker.history(period="1d",interval='1m')
tcs_df['Close'].plot(title="TCS's Stock Price")

fig = px.line(tcs_df,y='Close',title='TCS Share Price Over time')
fig.show()

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")
