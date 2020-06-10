"""class for Menu Item"""
class MenuItem:
    """initialize menu item"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def validate(self):
        """validate user input"""
        if self < 0 or self > 2:
            return False
        return True

    def info(self):
        """output menu"""
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        """add the price"""
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return round(total_price)
