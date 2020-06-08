# pylint: disable=C0114
from menu_item import MenuItem

class Food(MenuItem):  # pylint: disable=C0115
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    def calorie_info(self):  # pylint: disable=C0116
        print('kcal: ' + str(self.calorie_count))
