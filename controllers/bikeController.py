# Note Lars Van Kleef: De initialize basis
# -- Neer zetten eerste versie
# -- verwerken van de data in de database

from database import db


def addBikeToUser(requestData):
    '''Fiets toevoegen aan een gebruiker'''
    bike = db.addBikeToUser(
        requestData['user_id']
    )

    return {
        'bike': bike[0],
        'user_id': bike[-1]
    }

def getBikes(requestData):
    bikes = db.getBikesFromUser(requestData['user_id'])
    bikesList = []

    for bike in bikes:
        bikeDict = {}
        bikeDict.update({
            'bike_id': bike[0],
            'bike_uid': bike[1],
            'user_id': bike[-1]
        })
        bikesList.append(bikeDict)

    return bikesList