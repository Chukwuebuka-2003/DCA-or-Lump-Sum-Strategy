import yfinance as yf
su=yf.Ticker('GO0GL')

suy = su.history(period='10y')

import os
import pandas as pd
import datetime
from datetime import date, timedelta
today=date.today()

d1=today.strftime('%Y-%m-%d')
end_date=d1

d2=date.today()-timedelta(days=100)

d2=d2.strftime('%Y-%m-%d')

DATA_PATH= 'Googl_dataa.json'
if os.path.exists(DATA_PATH):
    with open (DATA_PATH)as f:
        suy=pd.read_json(DATA_PATH)


else:

    su=yf.Ticker('GOOGL')
    suy=su.history(period='10y')

    suy.to_json(DATA_PATH)


suy['Date'] = suy.index

attributes_container= []

print(suy.columns)

suy.to_csv('GOOGLE.csv',sep=',',index=False)

print(suy.tail())

    
