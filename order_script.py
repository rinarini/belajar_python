# pylint: disable=C0114
from food import Food
from drink import Drink
from menu_item import MenuItem

food1 = Food('Sandwich', 5, 330)
food2 = Food('Chocolate Cake', 4, 450)
food3 = Food('Cream Puff', 2, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 3, 180)
drink2 = Drink('Orange Juice', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]


def main():  # pylint: disable=C0116
    print('Food')
    index = 0
    for food in foods:
        print(str(index) + '. ' + food.info())
        index += 1

    print('Drinks')
    index = 0
    for drink in drinks:
        print(str(index) + '. ' + drink.info())
        index += 1

    print('--------------------')

    food_order = int(input('Enter food item number:(0-2) '))
    if MenuItem.validate(food_order):
        selected_food = foods[food_order]
        drink_order = int(input('Enter drink item number:(0-2) '))
        if MenuItem.validate(drink_order):
            selected_drink = drinks[drink_order]
            count = int(
                input('How many meals would you like to purchase? (10% off for 3 or more): '))
            result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
            print('Your total is $' + str(result))
        else:
            print('Please enter a valid number')
    else:
        print('Please enter a valid number')

if __name__ == '__main__':
    main()
