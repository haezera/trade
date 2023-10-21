import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.history(start="2023-01-01", end="2023-01-04"))

