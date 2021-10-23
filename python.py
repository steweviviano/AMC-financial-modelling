!pip install yfinance
!pip install pandas
!pip install streamlit


import streamlit as st
import yfinance as yf
import pandas as pd


st.title('Asset Management Challenge')
tickers = ('TSLA', 'APPL', 'MSFT', 'BTC-USD', 'ETH-USD')

dropdown = st.multiselect('Pick your assets',tickers)
start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0) # the cumulative return the first day would be NaN so we start from zero
    return cumret



if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])

    st.line_chart(df)
