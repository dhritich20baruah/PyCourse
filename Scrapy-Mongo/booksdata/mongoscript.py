from pymongo import MongoClient

# MongoDB connection
client = MongoClient("")
db = client["scrapy"]
collection = db["books"]