from datetime import date, timedelta
import logging
import os
import pandas as pd
import sys
import time
import yaml
import yfinance as yf
from cryptKing import CryptKing

__author__ = "Dennis Biber"


class CryptoObject(CryptKing):

    def __init__(self, cryptoSymbol):
        super(CryptoObject, self).__init__()
        self._cryptoSymbol = input("What crpyto do you want to look at? ")
        self._cryptoData = None
        self._Onemin = None
        self._Twomin = None
        self._Threemin = None
        self._Fourmin = None

        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
        self._handler = logging.StreamHandler()
        self._logger.addHandler(self._handler)
        self._handler.setFormatter(formatter)
        # self._logger.info("  --{0}--  \n".format(self._cryptoSymbol))
        # self.write_stdout("  --{0}--  \n".format(self._cryptoSymbol))


    def getCryptoData(self):
        #Setting the end date to today
        self._cryptoData = yf.download(tickers=self._cryptoSymbol, period = '1m')["Close"].values

    def get1min(self):
        self._Onemin = self._cryptoData

    def get2min(self):
        self._Twomin = self._Onemin

    def get3min(self):
        self._Threemin = self._Twomin

    def get4min(self):
        self._Fourmin = self._Threemin

    def printResults(self):
        print(self.cryptoData, self.Onemin, self.Twomin, self.Threemin, self.Fourmin)


def main():
    config_path = "crypto_config.yml"
    with open(config_path, "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    todays_date = date.today()
    if not os.path.exists("crypto_{0}".format(todays_date)):
        os.mkdir("crypto_{0}".format(todays_date))

    counter = 0
    CO = CryptoObject("SHIB-USD")
    while True:
        print("  --Running Program--  \n")
        # for stock in config["crypto_config"]:
        #     objectDict = {}
        #     tickerSymbol = config["crypto_config"][stock]["crypto_symbol"]
        CO.getCryptoData()
        if counter == 1:
            CO.get1min()
        elif counter == 2:
            CO.get2min()
            CO.get1min()
        elif counter == 3:
            CO.get3min()
            CO.get2min()
            CO.get1min()
        elif counter >= 4:
            CO.get4min()
            CO.get3min()
            CO.get2min()
            CO.get1min()
            CO.printResults()
        counter += 1
        time.sleep(60)


if __name__ == "__main__":
    main()