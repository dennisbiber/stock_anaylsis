import os
import yaml

class MakeConfig(object):

	#// This can be refactored into a parent class for making configs
	#// THen we can have child classes for the specific config.
	def __init__(self, filename):
		super(MakeConfig, self).__init__()
		self._filename = filename
		self._tickerSymbol = ""
		self._companyName = ""
		self._msg = ""

	#// Make a UI instead to input this info.
	#// Then output onto a canvas with Dash or Django or TKinter
	def getTickerSymbol(self):
		self._tickerSymbol = input("What is the ticker symbol: ")

	def getCompanyName(self):
		self._companyName = input("What is the Company Name")

	# TODO FIx this so the damn thing will work
	def getYmlFormat(self):
		self._msg = """
{0}: {
	ticker_symbol: {1}
}.
	
""".format(self._companyName, self._tickerSymbol)

	def putIntoFIle(self):
		file = open("ticker_config.yaml", "a") # append mode
		file.write(self._msg)
		file.close()


def main():

	MC = MakeConfig("ticker_config.yaml")
	MC.getTickerSymbol()
	MC.getCompanyName()
	MC.getYmlFormat()
	MC.putIntoFIle()



if __name__ == "__main__":
	main()