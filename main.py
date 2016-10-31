from Database import db

# this needs to run once!
db.createDb()

user = db.addUser(
    'Lars',
    'van',
    'Kleef',
    'Amerikalaan 199',
    '3514BR',
    'Utrecht'
)

print(user)

# Add a bike to a user
bike = db.addBikeToUser(user[0][0])
print(bike)

# Get a bike by uid ID
bikeUid = db.getBikeByUid(bike[0])
print(bikeUid[1])

# # Add a bike to the shed
if db.addBikeToShed(bikeUid[1], user[0][0]):
    print('bike in shed')
    if db.removeBikeFromShed(bikeUid[1]):
        print('bike from shed')