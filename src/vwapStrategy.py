import pandas as pd
import yfinance as yf
import smaStrategy as sma

# Function: is_business_day
# Description: This function will check if a given date is a business day
# Input: date - the date to check if it is a business day
# Output: True - if the date is a business day
#         False - if the date is not a business day
def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))


# Function: medianAveragePrice
# Description: This function will calculate the median average price for a given ticker
# Input: tickerData - the ticker data for the given ticker
#        startDate - the start date for the median average price
#        endDate - the end date for the median average price
# Output: medianAveragePrice - the median average price for the given ticker
def averagePrice(tickerData, startDate, endDate):
    try: 
        historicalData = tickerData.history(
            start=pd.Timestamp(startDate),
            end=pd.Timestamp(endDate)
        )
        lowSum = 0 
        closeSum = 0
        highSum = 0

        # Iterate through dataframe and add to opensum, closesum and highsum
        for i in range(len(historicalData)):
            lowSum += historicalData.iloc[i]['Low']
            highSum += historicalData.iloc[i]['High']
        # Calculate median average price
        averagePrice = (lowSum + highSum) / (2 * len(historicalData))
        return averagePrice
    except Exception as e:
        print(e)

    
# Function: vwapPriceAndVolumeSum
# Description: This function will calculate the vwap strategy for a given ticker
# Input: tickerData - the ticker data for the given ticker
#        startDate - the start date for the vwap strategy
#        endDate - the end date for the vwap strategy
# Output: vwapPriceSum - the vwap price sum for the given ticker
#         volumeSum - the volume sum for the given ticker
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
    except Exception as e:
        print(e)


# Function: vwapStrategy
# Description: This function will calculate the vwap strategy for a given ticker
# Input: tickerData - the ticker data for the given ticker
#        date - the date for the vwap strategy
# Output: vwapPriceSum - the vwap price sum for the given ticker
#         volumeSum - the volume sum for the given ticker
def vwapStrategy(tickerData, date):
    try: 
        # Find the three day vwap strategy and compare to the median price
        # which we define as (open + high + close) / 3
        # If the vwap price sum is greater than the median price, then we buy
        # If the vwap price sum is less than the median price, then we sell
        # If the vwap price sum is equal to the median price, then we hold

        dateSpread = 3
        while (
            sma.calculateBusinessDays(
                pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
                pd.Timestamp(date)) != 3
        ):
            dateSpread += 1
        startDate = pd.Timestamp(date) - pd.Timedelta(days=dateSpread)
        endDate = pd.Timestamp(date)
        vwapData = vwapPriceAndVolumeSum(tickerData, startDate, endDate)
        vwapPrice = (
            vwapData[0] *
            vwapData[1]) / (
                vwapData[1])
        avgPrice = averagePrice(tickerData, startDate, endDate)
        if vwapPrice > avgPrice:
            return 'BUY'
        elif vwapPrice < avgPrice:
            return 'SELL'
        else:
            return 'HOLD'

    except Exception as e:
        print(e)

