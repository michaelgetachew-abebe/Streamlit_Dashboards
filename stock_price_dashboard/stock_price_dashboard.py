# Import the core packages required for the project
import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price App")
st.header("GOOGLE & APPLE STOCK PRICE FROM ***2011-7-31*** TO ***2021-12-29***")
st.write("""
# Stock Price Appp

Shown are the stock ***closing price*** and ***volume*** of Google!!! 

""")
#define a ticker symbol
tickerSymbol_google = 'GOOGL'
tickerSymbol_apple = 'AAPL'
#get data on the ticker
tickerData_google = yf.Ticker(tickerSymbol_google)
tickerData_apple = yf.Ticker(tickerSymbol_apple)
#get the historical data for this ticker
ticker_df_google = tickerData_google.history(period="1d", start="2011-7-31", end = "2021-12-29")
ticker_df_apple = tickerData_apple.history(period = "1d", start="2011-7-31", end = "2021-12-29")
st.write("""
## Closing Price of Google
""")
st.line_chart(ticker_df_google.Close)

st.write("""
## Volume Price of Google
""")
st.line_chart(ticker_df_google.Volume)

st.write("""
## Closing Price of Apple
""")
st.line_chart(ticker_df_apple.Close)

st.write("""
## Volume Price of Apple
""")
st.line_chart(ticker_df_apple.Volume)