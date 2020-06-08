"""
class for Menu Item
"""
class MenuItem:  # pylint: disable=C0115
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def validate(self):  # pylint: disable=C0116
        if self < 0 or self > 2:
            return False
        return True

    def info(self):  # pylint: disable=C0116
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):  # pylint: disable=C0116
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return round(total_price)
