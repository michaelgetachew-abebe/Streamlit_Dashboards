# Import the core packages required for the project
import yfinance as yf
import streamlit as st
import pandas as pd

st.title("STOCK PRICE App")
st.header("GOOGLE")
st.write("""
# Stock Price Appp

Shown are the stock closing price and volume of Google!!! 

""")
#define a ticker symbol
tickerSymbol = 'GOOGL'
#get data on the ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical data for this ticker
ticker_df = tickerData.history(period="1d", start="2011-7-31", end = '2021-12-29')

st.line_chart(ticker_df.Close)

st.line_chart(ticker_df.Volume)
