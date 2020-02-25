import unittest

import currency
import exception


class CurrencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.currency = currency.Currency()

    def setUp(self):
        self.currency.set_currency_value('qwer', 'm')

    def tearDown(self):
        self.currency._currency_map = {}

    def test_set_currency_value(self):
        self.currency.set_currency_value('glob', 'i')
        self.assertDictEqual({'glob': 1, 'qwer': 1000}, self.currency._currency_map)

    def test_set_currency_value_with_exception(self):
        with self.assertRaises(exception.InvalidRomanNumber) as context:
            self.currency.set_currency_value('glob', 'p')
        self.assertEqual("'p' is invalid galactic number", context.exception.args[0])
        self.assertEqual(exception.InvalidRomanNumber, context.exception.__class__)

    def test_get_currency_value(self):
        currency_value = self.currency.get_currency_value('qwer')
        self.assertEqual(1000, currency_value)

    def test_get_currency_value_with_exception(self):
        with self.assertRaises(exception.InvalidCurrency) as context:
            self.currency.get_currency_value('iopt')
        self.assertEqual("'iopt' is invalid galactic number", context.exception.args[0])
        self.assertEqual(exception.InvalidCurrency, context.exception.__class__)

    def test_parse_currency(self):
        self.currency.set_currency_value('glob', 'i')
        response = self.currency.parse_currency(['glob', 'qwer'])
        self.assertEqual([1, 1000], response)

    def test_parse_currency_with_exception(self):
        with self.assertRaises(exception.InvalidCurrency) as context:
            self.currency.parse_currency(['glob', 'iopt'])
        self.assertEqual("'['glob', 'iopt']' is invalid galactic number", context.exception.args[0])
        self.assertEqual(exception.InvalidCurrency, context.exception.__class__)
