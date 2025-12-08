from utils.db import db
from bson.objectid import ObjectId
import datetime

def create_history(user_id, input_text, prediction, confidence, image_url=None):
    if db is None:
        return {'_id': 'mock_id'}
    history_col = db.get_collection('history')
    doc = {
        'userId': ObjectId(user_id),
        'inputText': input_text,
        'prediction': prediction,
        'confidence': float(confidence),
        'imageUrl': image_url,
        'createdAt': datetime.datetime.utcnow()
    }
    res = history_col.insert_one(doc)
    return history_col.find_one({'_id': res.inserted_id})

def get_history_for_user(user_id):
    if db is None:
        return []
    history_col = db.get_collection('history')
    return list(history_col.find({'userId': ObjectId(user_id)}).sort('createdAt', -1))
