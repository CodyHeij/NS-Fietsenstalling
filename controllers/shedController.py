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
                return db.addBikeToShed(bike[0])

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
                bikes = db.getBikesFromUser(user[0][0])

                bikeList = []

                for bike in bikes:
                    bikeList.append(bike[1])

                if len(bikes) >= 1 and requestData['bike_uid'] in bikeList:
                    bike = db.getBikeByUid(requestData['bike_uid'])
                    return db.removeBikeFromShed(bike[0])

                return False

            return False

        except:
            return False

    return False

def getShedHistory(requestData):
    '''Geeft een overzicht van alle keren dat een gebruiker zijn fiets heeft gestald in de fiets stalling'''
    bike = db.getBikeByUid(requestData['bike_uid'])
    shedHistory = db.getShedHistory(bike[0])

    shedHistoryList = []

    for item in shedHistory:
        itemDict = {}
        itemDict.update({
            'id': item[0],
            'bike_id': item[1],
            'start_time': item[2],
            'end_time': item[3]
        })
        shedHistoryList.append(itemDict)

    return shedHistoryList

def getFreePlaces():
    '''Geeft terug hoeveel vrije plekken er nog zijn in de stalling'''
    totalNumberOfPlaces = 1500

    try:
        places = db.getPlaces()
        return {'places': int(totalNumberOfPlaces - places[-1])}
    except:
        return False
