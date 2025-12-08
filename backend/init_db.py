#!/usr/bin/env python
"""
Initialize MongoDB database and collections for AI Fake News Detector.
Creates the database and collections if they don't exist.
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient, errors
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/aifakenews')
DB_NAME = MONGO_URI.split('/')[-1] if '/' in MONGO_URI else 'aifakenews'

def init_database():
    """Connect to MongoDB and create collections if they don't exist."""
    try:
        print(f"Connecting to MongoDB at {MONGO_URI}...")
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        
        # Test connection
        client.admin.command('ping')
        print("✓ MongoDB connection successful!")
        
        # Get database
        db = client.get_default_database()
        print(f"✓ Database: {db.name}")
        
        # Create collections if they don't exist
        collections_to_create = ['users', 'history']
        existing = db.list_collection_names()
        
        for collection_name in collections_to_create:
            if collection_name not in existing:
                db.create_collection(collection_name)
                print(f"✓ Created collection: {collection_name}")
            else:
                print(f"✓ Collection already exists: {collection_name}")
        
        # Create indexes for better query performance
        users_col = db.get_collection('users')
        users_col.create_index('email', unique=True)
        print("✓ Created unique index on users.email")
        
        history_col = db.get_collection('history')
        history_col.create_index('userId')
        history_col.create_index('createdAt')
        print("✓ Created indexes on history")
        
        print("\n✓ Database initialization complete!")
        return True
        
    except ServerSelectionTimeoutError:
        print("✗ ERROR: Could not connect to MongoDB at", MONGO_URI)
        print("  Make sure MongoDB is running. On Windows, you can:")
        print("    1. Install MongoDB Community Edition from https://www.mongodb.com/try/download/community")
        print("    2. Or use Docker: docker run -d -p 27017:27017 --name mongodb mongo:latest")
        print("    3. Or use MongoDB Atlas (cloud): https://www.mongodb.com/cloud/atlas")
        return False
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        return False

if __name__ == '__main__':
    success = init_database()
    exit(0 if success else 1)
