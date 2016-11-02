from tkinter import *
from Database import db

def addBike(master):
    global bikeToShedSuccess
    global firstNameTo
    global lastNameTo
    global bikeUidTo

    Message(master, text="Voeg een fiets to aan de stalling", width=200).grid(row=14, sticky=W, pady=4)

    Label(master, text="First Name").grid(row=15)
    Label(master, text="Last Name").grid(row=16)
    Label(master, text="Bike id").grid(row=17)

    firstNameTo = Entry(master, width=50)
    lastNameTo = Entry(master, width=50)
    bikeUidTo = Entry(master, width=50)

    firstNameTo.grid(row=15, column=1)
    lastNameTo.grid(row=16, column=1)
    bikeUidTo.grid(row=17, column=1)

    Button(master, text='Add', command=addBikeToShed).grid(row=18, column=1, sticky=W, pady=4)

    bikeToShedSuccess = StringVar()
    Message(master, text="Success:", width=100).grid(row=19)
    Message(master, textvariable=bikeToShedSuccess, width=100).grid(row=19, column=1)

def removeBike(master):
    global bikeFromShedSuccess
    global firstNameFrom
    global lastNameFrom
    global bikeUidFrom

    Message(master, text="Haal een fiets uit de stalling", width=200).grid(row=20, sticky=W, pady=4)

    Label(master, text="First Name").grid(row=21)
    Label(master, text="Last Name").grid(row=22)
    Label(master, text="Bike id").grid(row=23)

    firstNameFrom = Entry(master, width=50)
    lastNameFrom = Entry(master, width=50)
    bikeUidFrom = Entry(master, width=50)

    firstNameFrom.grid(row=21, column=1)
    lastNameFrom.grid(row=22, column=1)
    bikeUidFrom.grid(row=23, column=1)

    Button(master, text='Add', command=removeBikeFromShed).grid(row=24, column=1, sticky=W, pady=4)
    bikeFromShedSuccess = StringVar()
    Message(master, text="Success:", width=100).grid(row=25)
    Message(master, textvariable=bikeFromShedSuccess, width=100).grid(row=25, column=1)

def addBikeToShed():
    try:
        user = db.getUserByFirstAndLastName(firstNameTo.get(), lastNameTo.get())
        bike = db.addBikeToShed(bikeUidTo.get(), user[0][0])
        bikeToShedSuccess.set(bike)
    except:
        bikeToShedSuccess.set('Er is iets fout gegaan!')

def removeBikeFromShed():
    try:
        bike = db.removeBikeFromShed(bikeUidFrom.get())
        bikeToShedSuccess.set(bike)
    except:
        bikeToShedSuccess.set('Er is iets fout gegaan!')