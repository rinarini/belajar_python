"""main"""
from database import menu
from database import customers

class Customers:
    """add customers info"""
    def __init__(self, name, address):
        """ Customers name and address """
        self.name = name
        self.address = address

    def info(self):
        """ show cust info """
        print('Food delivery to : '+ self.name + ' in address :' + self.address)
        # print(phrase)
        self.add()

    def add(self):
        """ add cust info to db"""
        data = {"name": self.name, "address": self.address}
        customers.insert_one(data)
        print('Data added successfully')


def addcust():
    """ ask cust info """
    custname = str(input('Enter your name: '))
    custaddress = str(input('Enter your address: '))
    Customers(custname, custaddress).info()
    order()

def order():
    """ ask order """
    print('Our Menu:')
    for item in menu.find({}, {"_id": 0, "name": 1, "price": 1}):
        print('Name: ' + item["name"] + ', Price: $' + str(item["price"]))
    chosen = str(input('Enter food name: '))
    myquery = {"name": chosen}
    data = menu.find(myquery)
    for item in data:
        print('The price is: $ ' + item["price"])


def main():
    """ run main """
    print('Welcome!')
    addcust()
    print('Thank you for your order')


if __name__ == '__main__':
    main()
