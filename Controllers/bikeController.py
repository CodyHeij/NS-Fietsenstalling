from database import db

def addBikeToUser(requestData):
    bike = db.addBikeToUser(
        requestData['user_id']
    )

    return {
        'bike': bike[0],
        'user_id': bike[-1]
    }
