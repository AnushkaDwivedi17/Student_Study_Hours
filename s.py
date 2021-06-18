#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 01:52:00 2021

@author: anushkadwivedi
"""
import streamlit as st
import pandas_datareader as web

symbol = 'BSE/SPBSN5IP'
df = web.DataReader(symbol, 'quandl', api_key = 'Wzjxf7Z-SeZAj3zQ34cZ')
st.dataframe(df)
