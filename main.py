from Database import db

from Functions import register
from Functions import store
from Functions import request
from Functions import getInfo

def main():
    db.createDb()

    # Register user part
    register.registerUser()

    # Register a bike part
    register.registerBike()

    # Store a bike in the shed
    store.addBike()

    # Remove a bike form the shed
    request.requestBike()

    # Get info part
    getInfo.init()

    print("The application is started...")

if __name__ == "__main__":
    register.registerUser();