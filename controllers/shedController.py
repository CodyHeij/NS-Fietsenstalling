# Note Lars Van Kleef: De initialize basis
# -- Neer zetten simple bassis
# -- Verwerken van de data in de database

from database import db

def addBikeToShed(requestData):
    '''Verwerken en terug geven van True en False als de data verwerkt is'''
    if db.removeFreePlace() == True:

        bike = db.getBikeByUid(requestData['bike_uid'])

        try:
            if len(bike) >= 1:
                return db.addBikeToShed(requestData['bike_uid'])

            return False

        except:
            return False

    return False


def removeBikeFromShed(requestData):
    '''Verwerken en terug geven van True en False als de data verwerkt is'''
    user = db.getUserByFirstAndLastName(requestData['first_name'], requestData['last_name'])

    if db.addFreePlace() == True:
        try:
            if len(user) >= 1:
                bike = db.getBikeByUserId(user[0][0])

                if len(bike) >= 1:
                    return db.removeBikeFromShed(requestData['bike_uid'])

                return False

            return False

        except:
            return False

    return False

def getShedHistory(requestData):
    '''Geeft een overzicht van alle keren dat een gebruiker zijn fiets heeft gestald in de fiets stalling'''
    shedHistory = db.getShedHistory(requestData['user_id'])

    return shedHistory

def getFreePlaces():
    '''Geeft terug hoeveel vrije plekken er nog zijn in de stalling'''
    totalNumberOfPlaces = 1500

    try:
        places = db.getPlaces()
        return {'places': int(totalNumberOfPlaces - places[-1])}
    except:
        return False
