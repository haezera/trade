import yfinance as yf


class stock:
    def __init__(self, ticker):
        self.data = yf.Ticker(ticker)

    def history(self, startDate, endDate):
        return self.data.history(start=startDate, end=endDate)

    def incomeStmt(self):
        return self.data.income_stmt

    def balanceSheet(self):
        return self.data.balance_sheet

    def cashFlow(self):
        return self.data.cashflow
