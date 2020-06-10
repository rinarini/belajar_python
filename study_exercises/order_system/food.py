"""Food Class"""
from menu_item import MenuItem

class Food(MenuItem):
    """init food"""
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    def info(self):
        """output food info"""
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    def calorie_info(self):
        """output food calorie"""
        print('kcal: ' + str(self.calorie_count))
