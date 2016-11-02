from Database import db

# some init?
def init():
    return True

def registerUser(userData):
    user = db.addUser("Younes", "bbb", "Bannany", "Tomaatstraat 46", "3552GC", "Utrecht")
    registerBike(user[0], userData["bikeInfo"])


def registerBike(userId, bikeData):
    bike = db.addBikeToUser(user)
    return True
