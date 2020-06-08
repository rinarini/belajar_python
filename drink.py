# pylint: disable=C0114
from menu_item import MenuItem

class Drink(MenuItem):  # pylint: disable=C0115
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume
    def info(self):  # pylint: disable=C0116
        return self.name + ': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
