# Note Lars Van Kleef: De initialize basis
# -- Neer zetten simple bassis
# -- Verwerken van de data in de database

from database import db

def addBikeToShed(requestData):
    '''Verwerken en terug geven van True en False als de data verwerkt is'''
    return db.addBikeToShed(requestData['bike_uid'])

def removeBikeFromShed(requestData):
    '''Verwerken en terug geven van True en False als de data verwerkt is'''
    return db.removeBikeFromShed(requestData['bike_uid'])