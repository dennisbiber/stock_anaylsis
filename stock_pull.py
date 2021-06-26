from datetime import date, timedelta
import logging
import os
import pandas as pd
import sys
import yaml
import yfinance as yf

from stocKing import StocKing


class StockObject(StocKing):

	def __init__(self, tickerSymbol):
		super(StockObject, self).__init__()
		self._tickerSymbol = tickerSymbol
		self._history = None
		self._splits = None
		self._dividens = None
		self._balanceSheet = None

		logging.info("  --{0}--  \n".format(self._tickerSymbol))
		self.write_stdout("  --{0}--  \n".format(self._tickerSymbol))

	def getTickerData(self):
		self.tickerData = yf.Ticker(self._tickerSymbol)

	def getHistory(self):
		self._history = self.tickerData.history(period="max")
		logging.info("  --Stock History accessed--  \n")
		logging.info(self._history)

	def getSplits(self):
		self._file = self.tickerData.splits
		logging.info("  --Stock Splits accessed--  \n")
		logging.info(self._splits)

	def getDividends(self):
		self._dividends = self.tickerData.dividends
		logging.info("  --Dividens accessed--  \n")
		logging.info(self._dividens)

	def getBalanceSheet(self):
		self._balanceSheet = self.tickerData.balance_sheet
		logging.info("  --Balance Sheet accessed--  \n")
		logging.info(self._balanceSheet)


def main():
	config_path = "ticker_config.yaml"
	with open(config_path, "r") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)
	dataFrame = []
	for stock in config["stock_config"]:
		print("  --Running Program--  \n")
		objectDict = {}
		tickerSymbol = config["stock_config"][stock]["ticker_symbol"]
		sO = StockObject(tickerSymbol)
		sO.getTickerData() # trigger signal
		tickSym = sO.tickerSymbol
		print(f"{tickSym} history is being fetched.")
		w = pd.DataFrame(sO.setHistory)
		print(f"{tickSym} splits are being fetched.")
		x = pd.DataFrame(sO.setSplits)
		print(f"{tickSym} dividends are being fetched.")
		y = pd.DataFrame(sO.setDividends)
		print(f"{tickSym} balance sheet is being fetched.")
		z = pd.DataFrame(sO.setBalanceSheet)
		dataFrame.append([tickSym, w, x, y, z])

	import pprint
	pprint.pprint(dataFrame)


if __name__ == "__main__":
	main()