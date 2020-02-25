import exception

RULES = {
    frozenset((1,)): (set([5, 10]), '"I" can be subtracted from "V" and "X" only'),
    frozenset((10,)): (set([50, 100]),  '"X" can be subtracted from "L" and "C" only'),
    frozenset((100,)): (set([500, 1000]),  '"C" can be subtracted from "D" and "M" only'),
    frozenset((5,)): (set([]), '"V" can never be subtracted'),
    frozenset((50,)): (set([]), '"L" can never be subtracted'),
    frozenset((500,)): (set([]), '"D" can never be subtracted'),
}


def get_net_value(roman_values):
    """ Reduces roman values to single integer value. """
    total_value = 0
    while roman_values:
        roman_value = roman_values.pop(0)
        if roman_values and roman_values[0] > roman_value:
            if frozenset((roman_value,)) in RULES and roman_values[0] in RULES.get(frozenset((roman_value,)))[0]:
                total_value += (roman_values[0] - roman_value)
                roman_values.pop(0)
            else:
                raise exception.InvalidCurrencyRule(RULES.get(frozenset((roman_value,)))[1])
        else:
            total_value += roman_value
    return total_value
