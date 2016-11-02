from Database import db

def addBikeToShed(requestData):
    return db.addBikeToShed(requestData['bike_uid'], requestData['user_id'])

def removeBikeFromShed(requestData):
    return db.removeBikeFromShed(requestData['bike_uid'])