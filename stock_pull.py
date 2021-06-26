from datetime import date, timedelta
import logging
import os
import pandas as pd
import sys
import yaml
import yfinance as yf


class StockObject(object):

	def __init__(self, tickerSymbol):
		super(StockObject, self).__init__()
		self._tickerSymbol = tickerSymbol
		self._history = None
		self._splits = None
		self._dividens = None
		self._balanceSheet = None

		logging.info("  --{0}--  \n".format(self._tickerSymbol))
		write_stdout("  --{0}--  \n".format(self._tickerSymbol))

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

	@property
	def tickerSymbol(self):
		return self._tickerSymbol
	

	@property
	def setHistory(self):
		self.getHistory()
		return self._history

	@property
	def setSplits(self):
		self.getSplits()
		return self._splits

	@property
	def setDividends(self):
		self.getDividends()
		return self._dividends

	@property
	def setBalanceSheet(self):
		self.getBalanceSheet()
		return self._balanceSheet


def write_stderr(err_msg):
    '''
    Write an error message with command line coloring
    :param err_msg: The message to be written
    '''
    sys.stderr.write("{0}{1}".format(err_msg, os.linesep))


def write_stdout(msg):
    '''
    Writes a non-error message with command line coloring
    :param msg: The message to be written
    '''
    sys.stdout.write("{0}{1}".format(msg, os.linesep))


def main():
	config_path = "ticker_config.yaml"
	with open(config_path, "r") as file:
		config = yaml.load(file, Loader=yaml.FullLoader)
	dataFrame = []
	for stock in config["stock_config"]:
		write_stdout("  --Running Program--  \n")
		objectDict = {}
		tickerSymbol = config["stock_config"][stock]["ticker_symbol"]
		sO = StockObject(tickerSymbol)
		sO.getTickerData() # trigger signal
		tickSym = sO.tickerSymbol
		write_stdout(f"{tickSym} history is being fetched.")
		w = pd.DataFrame(sO.setHistory)
		write_stdout(f"{tickSym} splits are being fetched.")
		x = pd.DataFrame(sO.setSplits)
		write_stdout(f"{tickSym} dividends are being fetched.")
		y = pd.DataFrame(sO.setDividends)
		write_stdout(f"{tickSym} balance sheet is being fetched.")
		z = pd.DataFrame(sO.setBalanceSheet)
		dataFrame.append([tickSym, w, x, y, z])

	import pprint
	pprint.pprint(dataFrame)


if __name__ == "__main__":
	main()