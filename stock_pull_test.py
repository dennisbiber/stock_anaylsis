import unittest
from stock_pull import StockObject


class TestStockPull(unittest.TestCase):

	def setUp(self):
		"""setup class"""
		self.blah = {}
		self.SO = StockObject("ALF")

	def tearDown(self):
		"""tearDown if any"""

	def test_has_variable_args_asserted(self):
		self.assertTrue(hasattr(self.SO, "_tickerSymbol"))
		self.assertTrue(hasattr(self.SO, "_history"))
		self.assertTrue(hasattr(self.SO, "_splits"))
		self.assertTrue(hasattr(self.SO, "_dividends"))
		self.assertTrue(hasattr(self.SO, "_balanceSheet"))
		self.assertTrue(hasattr(self.SO, "_cashflow"))

	def test_init_to_none(self):
		self.assertIsNone(self.SO._history)
		self.assertIsNone(self.SO._splits)
		self.assertIsNone(self.SO._dividends)
		self.assertIsNone(self.SO._balanceSheet)
		self.assertIsNone(self.SO._cashflow)

	def test_has_functions(self):
		self.SO.getTickerData()
		self.assertTrue(hasattr(self.SO, "__init__"))
		self.assertTrue(hasattr(self.SO, "getTickerData"))
		self.assertTrue(hasattr(self.SO, "getHistory"))
		self.assertTrue(hasattr(self.SO, "getSplits"))
		self.assertTrue(hasattr(self.SO, "getDividends"))
		self.assertTrue(hasattr(self.SO, "getBalanceSheet"))
		self.assertTrue(hasattr(self.SO, "getCashflow"))
		self.assertTrue(hasattr(self.SO, "tickerSymbol"))
		self.assertTrue(hasattr(self.SO, "setHistory"))
		self.assertTrue(hasattr(self.SO, "setSplits"))
		self.assertTrue(hasattr(self.SO, "setDividends"))
		self.assertTrue(hasattr(self.SO, "setBalanceSheet"))
		self.assertTrue(hasattr(self.SO, "setCashflow"))

	def test_vars_not_none(self):
		self.SO.getTickerData()
		self.SO.setHistory
		self.SO.setSplits
		self.SO.setDividends
		self.SO.setBalanceSheet
		self.SO.setCashflow
		self.assertIsNotNone(self.SO._history)
		self.assertIsNotNone(self.SO._splits)
		self.assertIsNotNone(self.SO._dividends)
		self.assertIsNotNone(self.SO._balanceSheet)
		self.assertIsNotNone(self.SO._cashflow)

	def test_change_setters(self):
		self.SO._splits = {}
		with self.assertRaises(AttributeError):
			self.setSplits
		self.SO._history = {}
		with self.assertRaises(AttributeError):
			self.setHistory
		self.SO._dividens = {}
		with self.assertRaises(AttributeError):
			self.setDividends
		self.SO._cashflow = {}
		with self.assertRaises(AttributeError):
			self.setCashflow
		self.SO._balanceSheet = {}
		with self.assertRaises(AttributeError):
			self.setBalanceSheet


if __name__ == "__main__":
	unittest.main()