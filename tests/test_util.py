import unittest

import exception
import util


class UtilTest(unittest.TestCase):

    def test_get_net_value_with_subtraction(self):
        """ Tests MMVI """
        response = util.get_net_value([1000, 1000, 5, 1])
        self.assertEqual(2006, response)

    def test_set_metal_value(self):
        """ Tests III """
        response = util.get_net_value([1, 1, 1])
        self.assertEqual(3, response)

    def test_set_metal_value_mixed(self):
        """ Tests MCMXLIV """
        response = util.get_net_value([1000, 100, 1000, 10, 50, 1, 5])
        self.assertEqual(1944, response)

    def test_set_metal_value_invalid_V(self):
        """ Tests VM """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([5, 1000])
        self.assertEqual('"V" can never be subtracted', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_L(self):
        """ Tests LM """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([50, 1000])
        self.assertEqual('"L" can never be subtracted', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_D(self):
        """ Tests DM """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([500, 1000])
        self.assertEqual('"D" can never be subtracted', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_X(self):
        """ Tests MXM """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([1000, 10, 1000])
        self.assertEqual('"X" can be subtracted from "L" and "C" only', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_X1(self):
        """ Tests MXD """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([1000, 10, 500])
        self.assertEqual('"X" can be subtracted from "L" and "C" only', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_I(self):
        """ Tests MIL """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([1000, 1, 50])
        self.assertEqual('"I" can be subtracted from "V" and "X" only', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)

    def test_set_metal_value_invalid_I1(self):
        """ Tests MID """
        with self.assertRaises(exception.InvalidCurrencyRule) as context:
            util.get_net_value([1000, 1, 500])
        self.assertEqual('"I" can be subtracted from "V" and "X" only', context.exception.args[0])
        self.assertEqual(exception.InvalidCurrencyRule, context.exception.__class__)
