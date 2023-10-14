import os
import time
from stock import Stock
from helpers import analyseHelp, infoHelp, commandHelp
# DEFINES

intro = """
pytrading ver 0.0.1 by Haeohreum Kim
Anything from pytrading shall not be misconstrued as financial advice.

Acknowledgements to:
    ranaroussi - author of yfinance pip package, for the api which i used.
    cinar - creator of indicator ts, for the inspiration.
    i used indicatorts extensively in my previous trading algorithm attempts.
"""

commandLoop = """
Structure:
    command loop
        stock analysis
            simple moving average
            awesome oscillator
        stock info

Commands for command loop:
    help: the command you just used!
    return: return to a previous state (stock analysis -> command loop, etc.)
    analyse: analyse a stock, using different indicators
    info: get information about a stock back
"""

analyseLoop = """
Commands for analysis loop:
    help: the command you just used!
    return: return to a previous state
    sma: Use the simple moving average strategy
    awsm: Use the awesome oscillator strategy
"""

infoLoop = """
Dates must be given in: YYYY-MM-DD format.
Interval must be given in days, as an integer. 
Commands for info loop:
    incomestmt: prints income statement(s)
    balancesheet: prints balance sheet(s)
    cashflow: prints cash flow statement(s)
    historic <date> <interval>: prints historic price data, with date and interval.
"""

exitStatement = """
Thank you for using pytrading. See you next time!
"""

# Create main loop


def lobby_loop():
    in_lobby = True
    while in_lobby is True:
        os.system('clear')
        user_input = input('What would you like to do? (`help` for help!): ')
        if user_input == 'help':
            commandHelp()
        elif user_input == 'return':
            return 'exit'
        elif user_input == 'analyse':
            return 'analyse'
        elif user_input == 'info':
            return 'info'
        else:
            print("You chose an invalid command. Use 'help' for information!")
            time.sleep(2)


def allocateTicker():
    ticker_validated = False
    stock = ''
    while (ticker_validated is False):
        try:
            ticker = input('Please enter a stock ticker from NASDAQ/NYSE: ')
            stock = Stock(ticker)
            ticker_validated = True
            print(f"Asset {ticker} has been successfully loaded.")
        except RuntimeError:
            print("You have inputted an invalid ticker! Try again.")

    return stock 


def analyse_loop():
    stock = allocateTicker()
    inAnalysis = True 
    while inAnalysis is True:
        user_response = input("What would you like to do?: ('help' for help)")
        if user_response == 'help':
            analyseHelp()
        elif user_response == 'return':
            return 'lobby'
        elif user_response == ''


def info_loop():
    stock = allocateTicker()
    inInfo = True
    while inInfo is True:
        user_response = input("What would you like to do?: ('help' for help)")
        if user_response == 'help':
            infoHelp()
        elif user_response == ''


def main():
    print(intro)
    time.sleep(3)
    currentState = 'lobby'
    while currentState != 'exit':
        if currentState == 'lobby':
            currentState = lobby_loop()
        elif currentState == 'analyse':
            currentState = analyse_loop()
        elif currentState == 'info':
            currentState = analyse_loop()
    print(exitStatement)


stock = allocateTicker()

if __name__ == '__main__':
    main()
