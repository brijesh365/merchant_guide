import exception

SUBTRACTION_RULES = {
    frozenset((1,)): (set([5, 10]), '"I" can be subtracted from "V" and "X" only'),
    frozenset((10,)): (set([50, 100]),  '"X" can be subtracted from "L" and "C" only'),
    frozenset((100,)): (set([500, 1000]),  '"C" can be subtracted from "D" and "M" only'),
    frozenset((5,)): (set([]), '"V" can never be subtracted'),
    frozenset((50,)): (set([]), '"L" can never be subtracted'),
    frozenset((500,)): (set([]), '"D" can never be subtracted'),
}

REPEAT_RULES = {
    frozenset((1,)): (3, '"I" can be repeated 3 times max'),
    frozenset((10,)): (3, '"X" can be repeated 3 times max'),
    frozenset((100,)): (3, '"C" can be repeated 3 times max'),
    frozenset((1000,)): (3, '"M" can be repeated 3 times max'),
    frozenset((5,)): (1, '"V" can never be repeated'),
    frozenset((50,)): (1, '"L" can never be repeated'),
    frozenset((500,)): (1, '"D" can never be repeated'),
}


def get_net_value(roman_values):
    """ Reduces roman values to single integer value. """
    total_value = 0
    repeat_count = 1
    while roman_values:
        roman_value = roman_values.pop(0)
        key = frozenset((roman_value,))
        if roman_values and roman_values[0] > roman_value:
            repeat_count = 1
            if roman_values[0] in SUBTRACTION_RULES.get(key)[0]:
                total_value += (roman_values[0] - roman_value)
                roman_values.pop(0)
            else:
                raise exception.InvalidCurrencyRule(SUBTRACTION_RULES.get(key)[1])
        else:
            if roman_values and roman_values[0] == roman_value:
                repeat_count += 1
            else:
                repeat_count = 1
            if repeat_count <= REPEAT_RULES.get(key)[0]:
                total_value += roman_value
            else:
                raise exception.InvalidCurrencyRule(REPEAT_RULES.get(key)[1])
    return total_value
