from pymongo import MongoClient

client = MongoClient("0.0.0.0:27018")

database_apple = client.refurbApple

collection_product = database_apple['product']

cursor = collection_product.find()

print(cursor.count())
# for i in cursor:
#     print("--------------")
#     print(i)
