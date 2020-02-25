def get_net_value(roman_values):
    """ Reduces roman values to single integer value. """
    total_value = 0
    while roman_values:
        roman_value = roman_values.pop(0)
        if roman_values and roman_values[0] > roman_value:
            total_value -= roman_value
        else:
            total_value += roman_value
    return total_value
