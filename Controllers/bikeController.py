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