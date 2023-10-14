import yfinance as yf
import pandas as pd
import numpy as np


def fiveDayMA(tickerData, date):
    dateSpread = 5
    while (
        calculateBusinessDays(
            pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            pd.Timestamp(date)) != 10):  # Just to be sure with public holidays
        dateSpread = dateSpread + 1

    historicalData = tickerData.history(
            start=pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            end=pd.Timestamp(date))

    fiveDaySum = 0
    increment = 0
    while (increment < 5):
        fiveDaySum = fiveDaySum + historicalData.iat[increment, 3]
        increment = increment + 1

    return fiveDaySum / 30


def thirtyDayMA(tickerData, date):
    dateSpread = 30
    while (
        calculateBusinessDays(
            pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            pd.Timestamp(date)) != 35):  # Just to be sure with public holidays
        dateSpread = dateSpread + 1

    historicalData = tickerData.history(
            start=pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            end=pd.Timestamp(date))

    thirtyDaySum = 0
    increment = 0
    while (increment < 30):
        thirtyDaySum = thirtyDaySum + historicalData.iat[increment, 3]
        increment = increment + 1

    return thirtyDaySum / 30


def calculateBusinessDays(startData, endDate):
    return np.busday_count(
        startData.strftime('%Y-%m-%d'), endDate.strftime('%Y-%m-%d'))


def sma(tickerData, date):
    print(f"""Simple Moving Average Strategy:
Target Company: {tickerData}
Date: {date}""")
    # Current five/ten day moving average
    currFiveDayMA = fiveDayMA(tickerData, date)
    currThirtyDayMA = thirtyDayMA(tickerData, date)

    # Previous five/ten day moving average
    prevFiveDayMA = fiveDayMA(tickerData, date - pd.Timedelta(days=5))
    prevThirtyDayMA = thirtyDayMA(tickerData, date - pd.Timedelta(days=10))

    # Check if five day was trailing above ten day previously
    if (prevFiveDayMA > prevThirtyDayMA):
        if (currFiveDayMA > currThirtyDayMA):
            print("HOLD")
        else:
            print("SELL")
    else:
        if (currFiveDayMA > currThirtyDayMA):
            print("BUY")
        else:
            print("HOLD")

