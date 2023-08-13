import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Hello")

btc = yf.download("BTC-USD","2008-01-01","2023-08-12")

st.table(btc)


