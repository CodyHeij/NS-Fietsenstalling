from tkinter import *
from Database import db

# Lars van Kleef
def addBike(master):
    '''Create ui for add a bike to a user'''
    global firstName
    global lastName
    global success

    Message(master, text="Voeg een fiets toe aan een gebruiker", width=200).grid(row=8, sticky=W, pady=4)

    # Create the labels
    Label(master, text="First Name").grid(row=9)
    Label(master, text="Last Name").grid(row=10)

    # Add the entry points
    firstName = Entry(master, width=50)
    lastName = Entry(master, width=50)

    # Set in the grid
    firstName.grid(row=9, column=1)
    lastName.grid(row=10, column=1)

    Button(master, text='Register', command=registerBikeToShed).grid(row=11, column=1, sticky=W, pady=4)

    # Show bike id
    success = StringVar()
    Message(master, text="Bike UID:", width=100).grid(row=12)
    Message(master, textvariable=success, width=100).grid(row=12, column=1)

# Lars van Kleef
def registerBikeToShed():
    '''Try to add the bike to a user in the db'''
    try:
        user = db.getUserByFirstAndLastName(firstName.get(), lastName.get())
        bike = db.addBikeToUser(user[0][0])
        success.set(bike)
    except:
        success.set('Er is iets fout gegaan!')