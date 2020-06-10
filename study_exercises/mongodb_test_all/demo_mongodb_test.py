import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# output all database list
print(myclient.list_database_names())

# check if certain database exist > by name
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

# create collection
mycol = mydb["customers"]

# output all database list
print(mydb.list_collection_names())

# check if certain database exist > by name
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

# add record to collection
# mydict = {"name" : "John", "address" : "Highway 37" }
# x = mycol.insert_one(mydict)
# print(x)

# add new record + return _id field
# mydict = {"name": "Peter", "address": "Lowstreet 27"}
# x = mycol.insert_one(mydict)
# print(x.inserted_id)

# Insert Multiple Documents, with Specified IDs
# mylist = [
#   {"_id": 1, "name": "John", "address": "Highway 37"},
#   {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#   {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   {"_id": 5, "name": "Michael", "address": "Valley 345"},
#   {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#   {"_id": 9, "name": "Susan", "address": "One way 98"},
#   {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   {"_id": 12, "name": "William", "address": "Central st 954"},
#   {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)

# returns the first occurrence in the selection
# x = mycol.find_one()
# print(x)

# selects all documents in the collection
# No parameters in the find() method gives you the same result as SELECT * in MySQL.
# for x in mycol.find():
#   print(x)

# find() with parameter = Return Only Some Fields
# for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
#   print(x)
# for x in mycol.find({}, {"address": 0}):
#   print(x)

# test error (?) masih kurang ngerti
# You get an error if you specify both 0 and 1 values in the same object
# for x in mycol.find({}, {"name": 1, "address": 0}):
#   print(x)

# filter with find()
# myquery = {"address": "Mountain 21"}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)
print('------------------')

# query example:Find documents where the address starts with the letter "S" or higher
# myquery = {"address": {"$gt": "S"}}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# Find documents where the address starts with the letter "S"
# myquery = {"address": {"$regex": "^S"}}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# sort alphabetically
# mydoc = mycol.find().sort("__id")
# for x in mydoc:
#   print(x)

# Sort reverse alphabetically
# mydoc = mycol.find().sort("name", -1)
# for x in mydoc:
#   print(x)

# delete document (only the first one)
# myquery = {"address": "Mountain 21"}
# mycol.delete_one(myquery)
# print('deleted!')

# Delete Many Documents
# myquery = {"__id": "Mountain 21"}
# mycol.delete_many(myquery)
# print('deleted!')

# delete all docs in collection
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

# delete collection
# mycol.drop()

# update record
# myquery = {"address": "Sideway 1633"}
# newvalues = {"$set": {"name": "Viola"}}
# mycol.update_one(myquery, newvalues)

# update many records
# myquery = {"address": {"$regex": "^S"}}
# newvalues = {"$set": {"name": "Minnie"}}
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

# Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)

# change collection name
# mydb.food.rename("menu")
