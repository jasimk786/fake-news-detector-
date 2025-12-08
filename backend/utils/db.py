from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/aifakenews')

try:
    client = MongoClient(MONGO_URI)
    db = client.get_default_database()
    # Test connection
    client.admin.command('ping')
    # Do not expose Collection objects at module import time to avoid
    # accidental truthiness checks (PyMongo Collections raise on bool()).
    users = None
    history = None
except Exception as e:
    print(f"MongoDB connection failed: {e}")
    db = None
    users = None
    history = None
