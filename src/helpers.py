import os
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
        print(infoLoop)
        user_input = input('')
