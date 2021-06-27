from datetime import date, timedelta
import logging
import os
import pandas as pd
import sys
import yaml
import yfinance as yf
from datetime import date
from stocKing import StocKing


class StockObject(StocKing):

	def __init__(self, tickerSymbol):
		super(StockObject, self).__init__()
		self._tickerSymbol = tickerSymbol
		self._history = None
		self._splits = None
		self._dividends = None
		self._balanceSheet = None
		self._cashflow = None

		self._logger = logging.getLogger(__name__)
		self._logger.setLevel(logging.INFO)
		formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
		self._handler = logging.StreamHandler()
		self._logger.addHandler(self._handler)
		self._handler.setFormatter(formatter)
		self._logger.info("  --{0}--  \n".format(self._tickerSymbol))
		self.write_stdout("  --{0}--  \n".format(self._tickerSymbol))

	def getTickerData(self):
		self.tickerData = yf.Ticker(self._tickerSymbol)
		self.getHistory()
		self.getSplits()
		self.getDividends()
		self.getBalanceSheet()
		self.getCashflow()

	def getHistory(self):
		self._history = self.tickerData.history(period="max")
		self._logger.info("  --Stock History accessed--  \n")

	def getSplits(self):
		self._splits = self.tickerData.splits
		self._logger.info("  --Stock Splits accessed--  \n")

	def getDividends(self):
		self._dividends = self.tickerData.dividends
		self._logger.info("  --Dividens accessed--  \n")

	def getBalanceSheet(self):
		self._balanceSheet = self.tickerData.balance_sheet
		self._logger.info("  --Balance Sheet accessed--  \n")

	def getCashflow(self):
		self._cashflow = self.tickerData.cashflow
		self._logger.info("  --Balance Sheet accessed--  \n")


def main():
	config_path = "ticker_config.yaml"
	with open(config_path, "r") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)

	todays_date = date.today()
	if not os.path.exists("{0}".format(todays_date)):
		os.mkdir("{0}".format(todays_date))
	for stock in config["stock_config"]:
		print("  --Running Program--  \n")
		objectDict = {}
		tickerSymbol = config["stock_config"][stock]["ticker_symbol"]

		#// Initialize a new object
		sO = StockObject(tickerSymbol)
		sO.getTickerData() # trigger signal
		tickSym = sO.tickerSymbol

		#// create the DataFrames of each object
		# TODO make this a loop
		print(f"{tickSym} history is being fetched.")
		hSt = pd.DataFrame(sO.setHistory)
		if not hSt.empty:
			hSt.to_csv("{1}/{0}_history.csv".format(stock, todays_date))
		print(f"{tickSym} balance sheet is being fetched.")
		bS = pd.DataFrame(sO.setBalanceSheet)
		if not bS.empty:
			bS.to_csv("{1}/{0}_balance_sheet.csv".format(stock, todays_date))
		print(f"{tickSym} cashflow is being fetched")
		cF = pd.DataFrame(sO.setCashflow)
		if not cF.empty:
			cF.to_csv("{1}/{0}_cashflow.csv".format(stock, todays_date))

if __name__ == "__main__":
	main()