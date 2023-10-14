import os
import time
import stock
import yahoofinance as yf
# DEFINES

import defines

# Create main loop


def lobby_loop():
    inLobby = True
    while inLobby is True:
        os.system('clear')
        userInput = input('What would you like to do? (`help` for help!): ')
        if userInput == 'help':
            commandHelp()
        elif userInput == 'return':
            return 'exit'
        elif userInput == 'analyse':
            return 'analyse'
        elif userInput == 'info':
            return 'info'
        else:
            print("You chose an invalid command. Use 'help' for information!")


def commandHelp():
    os.system('clear')
    userInput = ''
    print("q to exit")
    while userInput != 'q':
        print(commandLoop)
        userInput = input('')


def allocateTicker():
    tickerValidated = False
    stock
    while (tickerValidated is False):
        try:
            ticker = input('Please enter a stock ticker from NASDAQ/NYSE: ')
            stock = Stock(ticker)
            tickerValidated = True 
        exception:
            print("You have inputted an invalid ticker! Try again.")
    
    return tickerValidated

def analyse_loop():
    stock = allocateTicker()
    inAnalysis = True 
    while inAnalysis is True: 
        

def info_loop():
    stock = allocateTicker()
    inInfo = True
    while inInfo is True:
        


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


if __name__ == '__main__':
    main()
