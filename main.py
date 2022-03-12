# Run "pip install pymongo" only for local server
# Run "pip install pymongo dnspython" for MongoDB Atlas

# Run "pip install python-dotenv" for storing connection string

from dotenv import load_dotenv
import os
from pymongo import MongoClient
import datetime
from bson.objectid import ObjectId

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

print(client.list_database_names())

db = client["python-mongodb"]
# Load python-mongodb database from MongoDB server

print(db.list_collection_names())

# todo_1 = {
#     "name": "John",
#     "text": "My first todo",
#     "amount": 3,
#     "status": "open",
#     "tags": ["python", "coding"],
#     "date": datetime.datetime.utcnow()
# }

todosCollection = db.todos
# Load todos collection from python-mongodb database

# result = todosCollection.insert_one(todo_1)

# todos_2 = [
#     {
#         "name": "Kevin",
#         "text": "My second todo",
#         "amount": 5,
#         "status": "open",
#         "tags": ["mongodb", "coding"],
#         "date": datetime.datetime.utcnow()
#     },
#     {
#         "name": "Mike",
#         "text": "My third todo",
#         "amount": 1,
#         "status": "open",
#         "tags": ["linux", "coding"],
#         "date": datetime.datetime.utcnow()
#     }
# ]

# result = todosCollection.insert_many(todos_2)

# result = todosCollection.find_one()

# result = todosCollection.find_one({"name": "Kevin"})

# result = todosCollection.find_one({"_id": ObjectId("6226a5b5cd040f4833ed2168")})

# print(result)

# results = todosCollection.find()
# This will find all documents

# results = todosCollection.find({"status": "open"})

# results = todosCollection.find({"amount": {"$gt": 2}}).sort("name")

# print(results)

# for result in results:
#     print(result)
# Consider to use for loop to print all documents, if using find function

# print(todosCollection.count_documents({}))

# print(todosCollection.count_documents({"tags": "python"}))

# print(todosCollection.count_documents({"amount": {"$lt": 4}}))

# result = todosCollection.delete_one({"_id": ObjectId("6226a5b5cd040f4833ed2168")})

# result = todosCollection.delete_many({"status": "done"})

# result = todosCollection.delete_many({})
# This will delete all documents

# result = todosCollection.update_one({"tags": "linux"}, {"$set": {"status": "done"}})
# The first param is what the document to be updated, the second param is the updated value
