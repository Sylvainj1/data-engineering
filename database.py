from pymongo import MongoClient

client = MongoClient("0.0.0.0:27018")

database_apple = client.refurbApple

collection_mac = database_apple["mac"]
collection_iphone = database_apple["iphone"]
collection_ipad = database_apple["ipad"]

# database_apple.collection_mac.insert({
#     "name": "iphone 8",
#     "capacity" : "64"
# })


print(database_apple.list_collection_names())
