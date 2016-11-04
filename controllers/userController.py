# Note Younes Bannany: De initialize basis
# -- Eerste opzet neer zetten van de logica

# Note Lars Van Kleef: Tweede versie
# -- Verder verwerken van de data
# -- Success tokens toegevoegd aan response
# -- Bikes get bikes functie toegevoegd

from database import db
from flask import jsonify


def addUser(requestData):
    '''Een gebruiker toevoegen aan de database en hier meteen een fiets aan koppelen.'''
    try:
        user = db.addUser(
            requestData['first_name'],
            requestData['middel_name'],
            requestData['last_name'],
            requestData['address'],
            requestData['zipcode'],
            requestData['city']
        )

        # Meteen een eerste fiets aan een nieuwe gebruiker toevoegen.
        bike = db.addBikeToUser(user[0][0])

        return {
            'success': 1,
            'bike_uid': bike[0],
            'user_id': int(user[0][0]),
            'first_name': user[0][1],
            'middel_name': user[0][2],
            'last_name': user[0][3],
            'address': user[0][4],
            'zipcode': user[0][5],
            'city': user[0][6]
        }
    except:
        return {
            'success': 0
        }


def getUser(requestData):
    '''Een gebruiker uit het systeem ophalen met een voor naam een achternaam'''
    try:
        user = db.getUserByFirstAndLastName(requestData['first_name'], requestData['last_name'])

        return {
            'success': 1,
            'user_id': int(user[0][0]),
            'first_name': user[0][1],
            'middel_name': user[0][2],
            'last_name': user[0][3],
            'address': user[0][4],
            'zipcode': user[0][5],
            'city': user[0][6]
        }

    except:
        return {
            'success': 0
        }