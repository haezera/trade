import pandas as pd
from smaStrategy import calculateBusinessDays


def medianMA(tickerData, date, spread):
    dateSpread = spread
    while (
            calculateBusinessDays(
                pd.Timestamp(date) -
                pd.Timedelta(
                    days=dateSpread),
                pd.Timestamp(date)) != spread +
            5):  # Just to be sure with public holidays
        dateSpread = dateSpread + 1

    historicalData = tickerData.history(
        start=pd.Timestamp(date) - pd.Timedelta(days=dateSpread),
        end=pd.Timestamp(date))

    cumsum = 0
    increment = 0
    while (increment < spread):
        cumsum = cumsum + (
            historicalData.iat[increment, 1] +
            historicalData.iat[increment, 2]) / 2
        increment = increment + 1

    return cumsum / spread


def ao(tickerData, date):
    print(f"{date} loaded")
    fiveDayMA = medianMA(tickerData, date, 5)
    thirtyFourDayMA = medianMA(tickerData, date, 34)
    print(f'Five day MA: {fiveDayMA} | Thirty four day MA: {thirtyFourDayMA}')
    if fiveDayMA - thirtyFourDayMA > 0:
        return 'BUY'
    elif fiveDayMA - thirtyFourDayMA < 0:
        return 'SELL'
    else:
        return 'HOLD/WAIT'
