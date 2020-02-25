import exception
import messages


class Metal:
    def __init__(self):
        self._metal_map = {}

    def set_metal_value(self, metal, cost, unit):
        if not cost.isdigit():
            raise exception.InvalidCost(messages.INVALID_COST % cost)
        self._metal_map[metal] = int(cost) / unit

    def get_metal_value(self, metal):
        metal_value = self._metal_map.get(metal)
        if not metal_value:
            raise exception.InvalidMetal(messages.INVALID_METAL % metal)
        return metal_value
