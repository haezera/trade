import os
import time
from stock import Stock
import helpers
import pandas as pd
# DEFINES

intro = """
pytrading ver 0.0.2 by Haeohreum Kim
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
    vwap <start date> <end date>: Use the volume weight average price strategy
    clear: Clears the terminal
"""

infoLoop = """
Dates must be given in: YYYY-MM-DD format.
Interval must be given in days, as an integer.
Commands for info loop:
    incomestmt: prints income statement(s)
    balancesheet: prints balance sheet(s)
    cashflow: prints cash flow statement(s)
    historic <date> <interval>: prints historic price data, with date and interval.
    quit - return to lobby
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
            helpers.commandHelp()
        elif user_input == 'return':
            return 'exit'
        elif user_input == 'analyse':
            return 'analyse'
        elif user_input == 'info':
            return 'info'
        elif user_input == 'backtest':
            return 'backtest'
        elif user_input == 'backtestExpo':
            return 'backtestExpo'
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
        user_response = input("What would you like to do?: ('help' for help) ")
        sub_strings = user_response.split()
        if user_response == 'help':
            helpers.analyseHelp()
        elif user_response == 'return':
            return 'lobby'
        elif sub_strings[0] == 'sma':
            actions = helpers.smaPeriod(
                stock.data,
                sub_strings[1],
                sub_strings[2])
            helpers.printer(actions)
        elif sub_strings[0] == 'awsm':
            actions = helpers.aoPeriod(
                stock.data,
                sub_strings[1],
                sub_strings[2]
            )
            helpers.printer(actions)
        elif sub_strings[0] == 'vwap':
            actions = helpers.vwapPeriod(
                stock.data,
                sub_strings[1],
                sub_strings[2]
            )
            helpers.printer(actions)
        elif sub_strings[0] == 'clear':
            os.system('clear')
        else:
            print("You have inputted an invalid argument! Try again.")
            time.sleep(2)


def info_loop():
    stock = allocateTicker()
    inInfo = True
    while inInfo is True:
        user_response = input("What would you like to do? ('help' for help): ")
        sub_strings = user_response.split()
        if user_response == 'help':
            helpers.infoHelp()
        elif sub_strings[0] == 'historic':
            print(stock.history(
                sub_strings[1],
                sub_strings[2]
            ))
        elif user_response == 'incomestmt':
            helpers.incomeStmtPrinter(stock.incomeStmt())
        elif user_response == 'balancesheet':
            helpers.balanceSheetPrinter(stock.balanceSheet())
        elif user_response == 'cashflow':
            helpers.cashFlowPrinter(stock.cashFlow())
        elif user_response == 'quit':
            return 'lobby'
        else:
            print("You have inputted an invalid command! Try again.")
            time.sleep(2)


def backtest_loop():
    state = "in_progress"
    while state == "in_progress":
        stock = allocateTicker()
        actions = helpers.backtestAnalysis(stock.data)
        if actions == "quit":
            return "lobby"


def backtestExport_loop():
    state = "in_progress"
    data = {
        'ticker': [],
        'strategy': [],
        'startDate': [],
        'endDate': [],
        'profit/loss': []
    }

    while state == "in_progress":
        stock = allocateTicker()
        data["ticker"].append(stock.ticker)
        actions = helpers.backtestExpoAnalysis(stock.data, data)
        if actions == "quit":
            data["ticker"].pop()
            break

    # Make pandas data frame + read to excel sheet
    export = pd.DataFrame.from_dict(data)
    file_name = input("What do you want your filename to be?: ")
    export.to_excel(f"{file_name}.xlsx")
    print("Your file has been successfully exported!")
    return "lobby"


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
            currentState = info_loop()
        elif currentState == 'backtest':
            currentState = backtest_loop()
        elif currentState == 'backtestExpo':
            currentState = backtestExport_loop()
    print(exitStatement)


if __name__ == '__main__':
    main()
