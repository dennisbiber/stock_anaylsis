#used to hide the attributes functions.

import sys
import os

__author__ = "Dennis Biber"

class StocKing(object):

    def __init__(self):
        super(StocKing, self).__init__()

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


    #// These would normally be in a library
    def write_stderr(self, err_msg):
        '''
        Write an error message with command line coloring
        :param err_msg: The message to be written
        '''
        sys.stderr.write("{0}{1}".format(err_msg, os.linesep))


    def write_stdout(self, msg):
        '''
        Writes a non-error message with command line coloring
        :param msg: The message to be written
        '''
        sys.stdout.write("{0}{1}".format(msg, os.linesep))