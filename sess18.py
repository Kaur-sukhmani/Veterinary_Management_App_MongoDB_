"""
    1. create account on atlas
    2. network access-> 0.0.0.0/0
    3. create database user and password
    4. navigate to collections-> create database and collection
"""
"""
    pip install pymongo
    pip install pymongo[srv]
"""
"""
    database
    connect
    driver->python
    uri ko copy kardo and paste it in this code
"""

import pymongo
import certifi  # pip install certifi | if SSL error

ca = certifi.where()

uri = "mongodb+srv://root:root123@cluster0.yoemesb.mongodb.net/?retryWrites=true&w=majority"
# client = pymongo.MongoClient(uri)
client = pymongo.MongoClient(uri, tlsCAFile=ca)  # if SSL error
# else
db = client['gwpds']
collections = db.list_collection_names()
# print(collections)
for collection in collections:
    print(collection)

documents = db['customer'].find()
# to fetch all collections fro  documents
for document in documents:
    print(document)
