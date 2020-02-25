import constants
import exception
import messages


class Currency:
    def __init__(self):
        self._currency_map = {}

    def set_currency_value(self, currency, roman_number):
        roman_value = constants.ROMAN_VALUE.get(roman_number)
        if roman_value:
            self._currency_map[currency] = roman_value
        else:
            raise exception.InvalidRomanNumber(messages.INVALID_GALATIC_NUMBER % roman_number)

    def parse_currency(self, currency_array):
        try:
            return [self.get_currency_value(currency) for currency in currency_array]
        except Exception:
            raise exception.InvalidCurrency(messages.INVALID_GALATIC_NUMBER % str(currency_array))

    def get_currency_value(self, currency):
        currency_value = self._currency_map.get(currency)
        if not currency_value:
            raise exception.InvalidCurrency(messages.INVALID_GALATIC_NUMBER % currency)
        return currency_value
