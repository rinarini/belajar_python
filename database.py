"""database"""
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

menu = mydb["menu"]
customers = mydb["customers"]

print(mydb.list_collection_names())

print('Connection to Database Established')
