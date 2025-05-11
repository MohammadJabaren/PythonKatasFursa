import unittest
from katas.stock_trader import max_profit

class TestStockTrader(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_increasing_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    def test_single_price(self):
        self.assertEqual(max_profit([10]), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_same_prices(self):
        self.assertEqual(max_profit([5, 5, 5, 5]), 0)

    def test_profit_at_end(self):
        self.assertEqual(max_profit([9, 8, 7, 1, 10]), 9)