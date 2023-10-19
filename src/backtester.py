import pandas as pd
import helpers
import yfinance as yf
import os 
backTestIntro = """
backtester version 0.0.1 by Haeohreum Kim
"""


def backTester(tickerData, dictOfActions):
    os.system('clear')
    print(backTestIntro)
    number_of_stock = int(input(
        "How much stock would you like to buy at each BUY signal?: "))
    stock_bought = 0
    basis_price = 0
    profit_loss = 0

    for x, y in dictOfActions.items():
        if y == 'BUY' or y == 'SELL':
            stock_price = tickerData.history(
                start=pd.Timestamp(x),
                end=pd.Timestamp(x) + pd.Timedelta(days=1)).iat[0, 3]
            if y == 'SELL':
                sale_price = stock_price * stock_bought
                profit_loss = profit_loss + (basis_price - sale_price)
                basis_price = 0
                stock_bought = 0
            elif y == 'BUY':
                stock_bought = stock_bought + number_of_stock
                basis_price = basis_price + stock_price * number_of_stock

    return profit_loss
