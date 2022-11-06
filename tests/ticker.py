import pandas as pd

from .context import yfinance as yf

import unittest

log_requests = False

if log_requests:
    import logging
    logging.basicConfig(level=logging.DEBUG)

class TestTicker(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getTz(self):
        tkrs = ["IMP.JO", "BHG.JO", "SSW.JO", "BP.L", "INTC"]
        for tkr in tkrs:
            # First step: remove ticker from tz-cache
            yf.utils.get_tz_cache().store(tkr, None)

            # Test:
            dat = yf.Ticker(tkr)
            tz = dat._get_ticker_tz(debug_mode=False, proxy=None, timeout=None)

            self.assertIsNotNone(tz)


class TestTickerEarnings(unittest.TestCase):

    def setUp(self):
        self.ticker = yf.Ticker("GOOGL")

    def tearDown(self):
        self.ticker = None

    def test_earnings_history(self):
        data = self.ticker.earnings_history
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.earnings_history
        self.assertIs(data, data_cached, "data not cached")

    def test_earnings(self):
        data = self.ticker.earnings
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.earnings
        self.assertIs(data, data_cached, "data not cached")

    def test_quarterly_earnings(self):
        data = self.ticker.quarterly_earnings
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.quarterly_earnings
        self.assertIs(data, data_cached, "data not cached")

    def test_earnings_forecasts(self):
        data = self.ticker.earnings_forecasts
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.earnings_forecasts
        self.assertIs(data, data_cached, "data not cached")


class TestTickerHolders(unittest.TestCase):

    def setUp(self):
        self.ticker = yf.Ticker("GOOGL")

    def tearDown(self):
        self.ticker = None

    def test_major_holders(self):
        data = self.ticker.major_holders
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.major_holders
        self.assertIs(data, data_cached, "data not cached")

    def test_institutional_holders(self):
        data = self.ticker.institutional_holders
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.institutional_holders
        self.assertIs(data, data_cached, "data not cached")

    def test_mutualfund_holders(self):
        data = self.ticker.mutualfund_holders
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.mutualfund_holders
        self.assertIs(data, data_cached, "data not cached")


class TestTickerBalanceSheet(unittest.TestCase):

    def setUp(self):
        self.ticker = yf.Ticker("GOOGL")

    def tearDown(self):
        self.ticker = None

    def test_balance_sheet(self):
        data = self.ticker.balance_sheet
        self.assertIsInstance(data, pd.DataFrame, "data has wrong type")
        self.assertFalse(data.empty, "data is empty")

        data_cached = self.ticker.balance_sheet
        self.assertIs(data, data_cached, "data not cached")



def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTicker('Test ticker'))
    suite.addTest(TestTickerEarnings('Test earnings'))
    suite.addTest(TestTickerHolders('Test holders'))
    suite.addTest(TestTickerBalanceSheet('Test balance sheet'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
