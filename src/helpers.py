import os
import smaStrategy
import aoStrategy
import pandas as pd
import pprint
import holidays
import backtester

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
    backtest: get backtesting information for a ticker and a strategy
    backtestExpo: export backtesting information to an excel sheet
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


def is_business_day(date):
    return bool(len(pd.bdate_range(date, date)))


def is_public_holiday(date):
    us_holidays = holidays.US()
    return date in us_holidays


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
    dictOfMoves = {}
    while movingDate != pd.Timestamp(endDate):
        if is_business_day(pd.Timestamp(movingDate)) and is_public_holiday(movingDate) != True:
            action = smaStrategy.sma(tickerData, movingDate)
            dictOfMoves[movingDate.strftime("%Y-%m-%d")] = action

        movingDate = movingDate + pd.Timedelta(days=1)

    return dictOfMoves


def smaPrinter(dictOfMoves):
    os.system('clear')
    print('q to exit')
    userInput = ''
    while userInput != 'q':
        pprint.PrettyPrinter(width=20).pprint(dictOfMoves)
        userInput = input('')


def aoPeriod(tickerData, startDate, endDate):
    movingDate = pd.Timestamp(startDate)
    dictOfMoves = {}
    while movingDate != pd.Timestamp(endDate):
        action = aoStrategy.ao(tickerData, movingDate)
        dictOfMoves[movingDate.strftime("%Y-%m-%d")] = action
        movingDate = movingDate + pd.Timedelta(days=1)
    return dictOfMoves


def aoPrinter(dictOfMoves):
    os.system('clear')
    print('q to exit')
    userInput = ''
    while userInput != 'q':
        pprint.PrettyPrinter(width=20).pprint(dictOfMoves)
        userInput = input('')


backtestHelp = """
sma <startDate> <endDate> - back tests the Simple Moving Average strategy
ao <startDate> <endDate> - back tests the Awesome Oscillator strategy
quit - quit the backtester, and go back to the lobby
"""


def backtestAnalysis(stockData):
    os.system('clear')
    state = "unchosen"
    while (state == "unchosen"):
        completed = False 
        while (completed == False):
            try:
                analysis = input("Which strategy would you like to test? ('help' for help): ")
                sub_strings = analysis.split()
                if sub_strings[0] == "sma":
                    actions = smaPeriod(
                        stockData,
                        sub_strings[1],
                        sub_strings[2]
                    )
                    completed = True
                    print(backtester.backTester(stockData, actions))
                elif sub_strings[0] == "ao":
                    actions = smaPeriod(
                        stockData,
                        sub_strings[1],
                        sub_strings[2]
                    )
                    completed = True
                    print(backtester.backTester(stockData, actions))
                elif analysis == "quit":
                    completed = True
                    return "quit"
                else:
                    print("You printed an invalid command. Try again!")
            except:
                print("There has been a runtime error. Try again!")


def backtestExpoAnalysis(stockData, data):
    os.system('clear')
    state = "unchosen"
    sub_strings = []
    while (state == "unchosen"):
        completed = False 
        while (completed == False):
            try:
                analysis = input("Which strategy would you like to test? ('help' for help): ")
                sub_strings = analysis.split()
                if sub_strings[0] == "sma":
                    actions = smaPeriod(
                        stockData,
                        sub_strings[1],
                        sub_strings[2]
                    )
                    data["strategy"].append("sma")
                    data["startDate"].append(sub_strings[1])
                    data["endDate"].append(sub_strings[2])
                    data["profit/loss"].append(backtester.backTester(stockData, actions))
                    completed = True
                    return
                elif sub_strings[0] == "ao":
                    actions = smaPeriod(
                        stockData,
                        sub_strings[1],
                        sub_strings[2]
                    )
                    data["startegy"].append("ao")
                    data["startDate"].append(sub_strings[1])
                    data["endDate"].append(sub_strings[2])
                    data["profit/loss"].append(backtester.backTester(stockData, actions))
                    completed = True
                    return
                elif sub_strings[0] == "quit":
                    return "quit"
                else:
                    print("You printed an invalid command. Try again!")
            except:
                print("There has been a runtime error. Please try again!")
