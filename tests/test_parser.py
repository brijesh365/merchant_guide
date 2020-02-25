import unittest
import message_parser


class ParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = message_parser.Parser()

    def test_parse_message_with_rule1(self):
        response = self.parser.parse_message_with_rule1('how much is pish tegj glob glob ?')
        self.assertListEqual(['pish', 'tegj', 'glob', 'glob'], response)

    def test_parse_message_with_rule1_invalid(self):
        response = self.parser.parse_message_with_rule1('how much is pish tegj glob glob')
        self.assertListEqual([], response)

    def test_parse_message_with_rule2(self):
        response = self.parser.parse_message_with_rule2('how many credits is glob prok silver ?')
        self.assertListEqual(['glob', 'prok', 'silver'], response)

    def test_parse_message_with_rule2_invalid(self):
        response = self.parser.parse_message_with_rule2('how many credits is glob prok silver')
        self.assertListEqual([], response)

    def test_parse_message_with_rule3(self):
        response = self.parser.parse_message_with_rule3('glob is i')
        self.assertListEqual(['glob', 'i'], response)

    def test_parse_message_with_rule3_invalid(self):
        response = self.parser.parse_message_with_rule3('glob iis i')
        self.assertListEqual([], response)

    def test_parse_message_with_rule4(self):
        response = self.parser.parse_message_with_rule4('glob glob silver is 34 credits')
        self.assertListEqual(['silver', '34', ['glob', 'glob']], response)

    def test_parse_message_with_rule4_invalid(self):
        response = self.parser.parse_message_with_rule4('glob glob silver is 34 credites')
        self.assertListEqual([], response)