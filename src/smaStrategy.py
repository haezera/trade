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

    return fiveDaySum / 5


def tenDayMA(tickerData, date):
    dateSpread = 10
    while (
        calculateBusinessDays(
            pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            pd.Timestamp(date)) != 15):  # Just to be sure with public holidays
        dateSpread = dateSpread + 1

    historicalData = tickerData.history(
            start=pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
            end=pd.Timestamp(date))

    tenDaySum = 0
    increment = 0
    while (increment < 10):
        tenDaySum = tenDaySum + historicalData.iat[increment, 3]
        increment = increment + 1

    return tenDaySum / 10


def calculateBusinessDays(startData, endDate):
    return np.busday_count(
        startData.strftime('%Y-%m-%d'), endDate.strftime('%Y-%m-%d'))


def sma(tickerData, date):
    print(f"{date} loaded")
    # Current five/ten day moving average
    currFiveDayMA = fiveDayMA(tickerData, date)
    currTenDayMA = tenDayMA(tickerData, date)

    # Previous five/ten day moving average
    prevFiveDayMA = fiveDayMA(tickerData, date - pd.Timedelta(days=5))
    prevTenDayMA = tenDayMA(tickerData, date - pd.Timedelta(days=10))
    # Check if five day was trailing above ten day previously
    if (prevFiveDayMA > prevTenDayMA):
        if (currFiveDayMA > currTenDayMA):
            return 'HOLD/WAIT'
        else:
            return 'BUY'
    else:
        if (currFiveDayMA > currTenDayMA):
            return 'SELL'
        else:
            return 'HOLD/WAIT'
