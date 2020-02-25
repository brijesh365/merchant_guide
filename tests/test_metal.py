import unittest

import metals
import exception


class MetalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metal = metals.Metal()

    def setUp(self):
        self.metal.set_metal_value('gold', '68', 1)

    def tearDown(self):
        self.metal._metal_map = {}

    def test_set_metal_value(self):
        self.metal.set_metal_value('silver', '57800', 2)
        self.assertDictEqual({'silver': 28900, 'gold': 68}, self.metal._metal_map)

    def test_set_metal_value_with_exception(self):
        with self.assertRaises(exception.InvalidCost) as context:
            self.metal.set_metal_value('silver', 'invalid cost', 2)
        self.assertEqual("'invalid cost' is invalid numeric value", context.exception.args[0])
        self.assertEqual(exception.InvalidCost, context.exception.__class__)

    def test_get_metal_value(self):
        currency_value = self.metal.get_metal_value('gold')
        self.assertEqual(68, currency_value)

    def test_get_metal_value_with_exception(self):
        with self.assertRaises(exception.InvalidMetal) as context:
            self.metal.get_metal_value('iron')
        self.assertEqual("I've no idea of the trading metal iron", context.exception.args[0])
        self.assertEqual(exception.InvalidMetal, context.exception.__class__)