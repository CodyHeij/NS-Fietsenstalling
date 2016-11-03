from database import db

def addBikeToShed(requestData):
    return db.addBikeToShed(requestData['bike_uid'])

def removeBikeFromShed(requestData):
    return db.removeBikeFromShed(requestData['bike_uid'])
