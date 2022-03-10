
import unittest
import unittest.mock
import configparser
import sys
sys.path.insert(0, '..')
from maeapi.maeapi import MAE  # noqa: E402

config = configparser.RawConfigParser()
config.read('./test.cfg', 'utf-8')

class TestMAE(unittest.TestCase):   
    @classmethod
    def setUpClass(cls):
        cls.mae = MAE(config['auth']['headers_file'])

    def test_init(self):
        self.assertRaises(Exception, MAE, "{}")

    def test_get_spending_patterns(self):
        result = self.mae.get_spending_patterns('20220101')
        self.assertTrue(len(result))

    def test_get_transaction_history(self):
        result = self.mae.get_transaction_history('20220101', '20220201')
        self.assertTrue(len(result))

    def test_get_primary_summary_balance(self):
        message, result = self.mae.get_primary_summary_balance()
        self.assertEqual(message, 'success')
        self.assertTrue(len(result))

    def test_get_all_summary_balance(self):
        message, result = self.mae.get_all_summary_balance()
        self.assertEqual(message, 'success')
        self.assertTrue(len(result))
        print(result)

if __name__ == '__main__':
    unittest.main()