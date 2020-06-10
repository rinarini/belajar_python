"""Drink Class"""
from menu_item import MenuItem

class Drink(MenuItem):
    """init drink"""
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume
    def info(self):
        """output info"""
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
