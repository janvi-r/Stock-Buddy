import yfinance as yf
from StocksClass import Stocks

stock = Stocks("AAPL", 10)  # symbol = "AAPL", quantity = 10

# Print details using __str__
print(stock)

# Access some attributes or methods
print("Symbol:", stock.getSymbol())
print("Name:", stock.getName())
print("Price:", stock.getPrice())
print("Total value:", stock.get_value())

# Change symbol to test setSymbol()
stock.setSymbol("TSLA")
print(stock)
#how to make apple stock a class object

# def setStockInfo(self, name = stock_name, price = stock_price):
#     self.stock_name = name
#     self.stock_price = price


# apple.setName(self, name="Apple Inc.")
# print(apple.getName(self))
# # def getStockInfo(self, )