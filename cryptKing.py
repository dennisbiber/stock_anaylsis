import sys
import os

__author__ = "Dennis Biber"


class CryptKing(object):

    def __init__(self):
        super(CryptKing, self).__init__()

    @property
    def cryptoData(self):
        return self._cryptoData

    @property
    def Onemin(self):
        return self._Onemin

    @property
    def Twomin(self):
        return self._Twomin  
    
    @property
    def Threemin(self):
        return self._Threemin

    @property
    def Fourmin(self):
        return self._Fourmin

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