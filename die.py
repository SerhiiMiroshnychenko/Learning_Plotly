from random import randint


class Die:
    """Клас репрезентує один кубик"""

    def __init__(self, num_sides=6):
        """Визначити кубик із шістьома гранями"""
        self.num_sides = num_sides

    def roll(self):
        """Повернути випадкове значення від 1 до 6"""
        return randint(1, self.num_sides)

