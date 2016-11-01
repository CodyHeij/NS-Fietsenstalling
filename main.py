from Database import db

from Functions import register
from Functions import store
from Functions import request
from Functions import getInfo

db.createDb()


# Register user part
register.registerUser()

# Register a bike part
register.registerBike()

# Store a bike in the shed
store.addBike()

# Remove a bike form the shed
request.getBike()

# Get info part
getInfo.init()
