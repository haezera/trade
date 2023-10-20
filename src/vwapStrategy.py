import pandas as pd
import yfinance as yf
import smaStrategy as sma

def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))


# Function: vwapStrategy
# Description: This function will calculate the vwap strategy for a given ticker
# Input: tickerData - the ticker data for the given ticker
#        startDate - the start date for the vwap strategy
#        endDate - the end date for the vwap strategy
# Output: vwapStrategy - the vwap strategy for the given ticker
def vwapPriceAndVolumeSum(tickerData, startDate, endDate):
    try:
        historicalData = tickerData.history(
            start=pd.Timestamp(startDate),
            end=pd.Timestamp(endDate)
        )
        rowLength = len(historicalData)
        highSum = 0
        lowSum = 0
        closeSum = 0
        volumeSum = 0
        # Iterate through dataframe and add to highsum, lowsum and closesum
        for i in range(rowLength):
            highSum += historicalData.iloc[i]['High']
            lowSum += historicalData.iloc[i]['Low']
            closeSum += historicalData.iloc[i]['Close']
            volumeSum += historicalData.iloc[i]['Volume']
        # Calculate vwap price sum
        vwapPriceSum = (highSum + lowSum + closeSum) / (3 * rowLength)
        return (vwapPriceSum, volumeSum)
    except:
        print("Error: Could not calculate vwap price sum")


