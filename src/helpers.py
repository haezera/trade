import os
import smaStrategy
import pandas as pd
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
    sma <start date> <end date>: Use the simple moving average strategy
    awsm <start date> <end date>: Use the awesome oscillator strategy
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


def commandHelp():
    os.system('clear')
    user_input = ''
    print("q to exit")
    while user_input != 'q':
        print(commandLoop)
        user_input = input('')


def analyseHelp():
    os.system('clear')
    user_input = ''
    print("q to exit")
    while user_input != 'q':
        print(analyseLoop)
        user_input = input('')


def infoHelp():
    os.system('clear')
    user_input = ''
    print("q to exit")
    while user_input != 'q':
        print(infoLoop, end='\r')
        user_input = input('')


def incomeStmtPrinter(incomeStmt):
    os.system('clear')
    print("q to exit")
    user_input = ''
    while user_input != 'q':
        print(incomeStmt, end='\r')
        user_input = input('')


def balanceSheetPrinter(balanceSheet):
    os.system('clear')
    print("q to exit!")
    user_input = ''
    while user_input != 'q':
        print(balanceSheet, end='\r')
        user_input = input('')


def cashFlowPrinter(cashFlow):
    os.system('clear')
    print("q to exit!")
    user_input = ''
    while user_input != 'q':
        print(cashFlow, end='\r')
        user_input = input('')


def smaPeriod(tickerData, startDate, endDate):
    movingDate = pd.Timestamp(startDate)
    dictOfMoves = ''
    while (startDate is not endDate):
        action = smaStrategy.sma(tickerData, movingDate)
        dictOfMoves[movingDate] = action
        movingDate = movingDate + pd.Timedelta(days=1)
    return dictOfMoves


def smaPrinter(dictOfMoves):
    print('q to exit')
    userInput = ''
    while userInput != 'q':
        print(dictOfMoves)
        userInput = input('')
