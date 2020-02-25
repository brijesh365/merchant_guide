import unittest

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
