from utils.db import db
from bson.objectid import ObjectId

def create_user(name, email, password_hash):
    # Prefer accessing collection via db to avoid module-level collection truthiness issues
    if db is None:
        return {'_id': 'mock_id', 'name': name, 'email': email}
    users_col = db.get_collection('users')
    doc = { 'name': name, 'email': email, 'password': password_hash, 'themePreference': 'dark' }
    res = users_col.insert_one(doc)
    return users_col.find_one({'_id': res.inserted_id})

def find_by_email(email):
    print(f"DEBUG: find_by_email called; db={db}")
    if db is None:
        print("DEBUG: db is None")
        return None
    users_col = db.get_collection('users')
    print(f"DEBUG: users_col type={type(users_col)}")
    return users_col.find_one({'email': email})

def find_by_id(user_id):
    if db is None:
        return None
    users_col = db.get_collection('users')
    return users_col.find_one({'_id': ObjectId(user_id)})

def update_user(user_id, update):
    if db is None:
        return {'_id': user_id, 'name': 'Mock User', 'email': 'mock@test.com'}
    users_col = db.get_collection('users')
    users_col.update_one({'_id': ObjectId(user_id)}, {'$set': update})
    return find_by_id(user_id)
