import currency
import exception
import messages
import metals
import util


class Parser:
    def __init__(self):
        self.currency = currency.Currency()
        self.metal = metals.Metal()

    def parse_message(self, line):
        line = line.strip().lower()

        response = self.parse_message_with_rule1(line)
        if response:
            self.calculate_roman_value(response)
            return

        response = self.parse_message_with_rule2(line)
        if response:
            self.calculate_metal_cost(response)
            return

        response = self.parse_message_with_rule3(line)
        if response:
            self.currency.set_currency_value(response[0], response[1])
            return

        response = self.parse_message_with_rule4(line)
        if response:
            metal, cost, currency_codes = response
            try:
                roman_values = self.currency.parse_currency(currency_codes)
                unit = util.get_net_value(roman_values)
                self.metal.set_metal_value(metal, cost, unit)
            except (exception.InvalidCurrency, exception.InvalidCost) as e:
                print(e.args[0])
            return
        else:
            print(messages.NO_IDEA)

    def parse_message_with_rule1(self, line):
        if line.startswith("how much is") and line.endswith("?"):
            words = line.split()
            return words[3:-1]
        return []

    def parse_message_with_rule2(self, line):
        if line.startswith("how many credits is") and line.endswith("?"):
            return line.split()[4:-1]
        return []

    def parse_message_with_rule3(self, line):
        words = line.split()
        if len(words) == 3 and words[1] == "is":
            return [words[0], words[2]]
        return []

    def parse_message_with_rule4(self, line):
        words = line.split()
        if len(words) > 4 and words[-1] == "credits" and words[-3] == "is":
            words = words[:-1]
            cost = words[-1]
            words = words[:-2]
            metal = words.pop()
            return [metal, cost, words]
        return []

    def calculate_roman_value(self, currency_codes):
        try:
            roman_values = self.currency.parse_currency(currency_codes)
        except currency.InvalidCurrency as e:
            print(e.args[0])
        else:
            net_value = util.get_net_value(roman_values)
            print(" ".join(currency_codes), "is", net_value)

    def calculate_metal_cost(self, words):
        metal = words.pop()
        try:
            roman_values = self.currency.parse_currency(words)
            calculated_unit = util.get_net_value(roman_values)
            metal_value = self.metal.get_metal_value(metal)
        except (exception.InvalidCurrency, exception.InvalidMetal) as e:
            print(e.args[0])
        else:
            print(
                " ".join(words),
                metal.title(),
                "is",
                int(calculated_unit * metal_value),
                "Credits"
            )



