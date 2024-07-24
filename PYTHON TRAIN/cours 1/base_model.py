from typing import Tuple, List, Dict, Union, Any, Optional, Iterable, Callable
import os
from os.path import abspath, join

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot as plt
import numpy as np


current_directory = os.getcwd()
print(abspath(current_directory))

df_MSFT = pd.read_csv("MSFT_data.csv", index_col="Date", parse_dates=True)
close_prices = df_MSFT["Close"]

# Check for stationarity
def check_stationarity(timeseries):
    print("Results of Dickey-Fuller Test:")
    dftest = adfuller(timeseries)
    dftype = dftest[0]
    pvalue = dftest[1]

    print(f"Test Statistic: {dftype:.4f}")
    print(f"p-Value: {pvalue:.4f}")
    print("Critical Values:")
    for key, value in dftest[4].items():
        print(f"\t{key}: {value:.4f}")

    if pvalue < 0.05:
        print("The time series is likely stationary.")
        return True
    else:
        print("The time series is likely non-stationary.")
        return False


if not check_stationarity(close_prices):
    close_prices = close_prices.diff().dropna() 


check_stationarity(close_prices)

# Define the ARIMA model using the past 5 closing prices (p=5)
model = ARIMA(close_prices, order=(5, 1, 0))

# Fit the model to the data
model_fit = model.fit()

# Print the model summary
print(model_fit.summary())

# Forecast future stock prices for a specific number of periods (e.g., 252 for the next year)
forecast_horizon = 252
forecast = model_fit.forecast(steps=forecast_horizon)

# Optionally, plot the actual close prices and forecasts (in original units)
plt.figure(figsize=(12, 6))
plt.plot(close_prices, label="Actual Close Prices")
plt.plot(pd.date_range(start=close_prices.index[-1], periods=forecast_horizon, freq='B'), forecast, label="Forecasted Prices", color='red')
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.title("MSFT Stock Price Forecast for Next Year")
plt.show()

# To visualize the last 300 days with the forecast
last_300_days = close_prices.iloc[-30:]

plt.figure(figsize=(12, 6))
plt.plot(last_300_days, label="Actual Close Prices")
plt.plot(pd.date_range(start=last_300_days.index[-1], periods=forecast_horizon, freq='B'), forecast, label="Forecasted Prices", color='red')
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.title("MSFT Stock Price Forecast for Last 300 Days and Next Year")
plt.show()
