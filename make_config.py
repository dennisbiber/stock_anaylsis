import os
import yaml

class MakeConfig(object):

    #// This can be refactored into a parent class for making configs
    #// THen we can have child classes for the specific config.
    def __init__(self, fileName, makeType):
        super(MakeConfig, self).__init__()
        self._fileName = fileName
        self._makeType = makeType
        self._tickerSymbol = ""
        self._companyName = ""
        self._msg = ""

    #// Make a UI instead to input this info.
    #// Then output onto a canvas with Dash or Django or TKinter
    def getTickerSymbol(self):
        self._tickerSymbol = input("What is the ticker symbol: ")

    def getCompanyName(self):
        self._companyName = input("What is the Company Name: ")

    # TODO FIx this so the damn thing will work
    def getYmlFormat(self):
        tS = {}
        tS = "{0}: '{1}'".format(self._makeType, self._tickerSymbol)
        tS = "{\n    " + tS + "\n  }"
        self._msg = ",\n  {0}: {1}".format(self._companyName, tS)
        self._msg = "}" + self._msg
        print(self._msg)

    def removeBrackets(self):

        def get_size(fileobject):
            fileobject.seek(0,2) # move the cursor to the end of the file
            size = fileobject.tell()
            return size
        with open(self._fileName, "rb+") as file:
            file.seek(-1, os.SEEK_END)
            file.seek(-1, os.SEEK_CUR)
            filesize = get_size(file)
            file.truncate(filesize - 2)
            file.seek(-1, os.SEEK_END)
            file.truncate(filesize - 2)

    def putIntoFIle(self):
        file = open(self._fileName, "a") # append mode
        file.write(self._msg + "\n}")
        file.close()


def main():

    makeType = input("1) For stock\n2) For crypto: ")
    if makeType == "1":
        MC = MakeConfig("stock_config.yml", "stock_symbol")
    elif makeType == "2":
        MC = MakeConfig("crypto_config.yml", "crypto_symbol")
    MC.getTickerSymbol()
    MC.getCompanyName()
    MC.removeBrackets()
    MC.removeBrackets()
    MC.getYmlFormat()
    MC.putIntoFIle()



if __name__ == "__main__":
    main()