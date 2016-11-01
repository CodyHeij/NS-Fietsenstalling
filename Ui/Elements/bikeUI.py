from tkinter import *
from Database import db

def addBike(master):
    global firstName
    global lastName

    Label(master, text="First Name").grid(row=8)
    Label(master, text="Last Name").grid(row=9)

    firstName = Entry(master)
    lastName = Entry(master)

    firstName.grid(row=8, column=1)
    lastName.grid(row=9, column=1)

    Button(master, text='Register', command=registerBikeToShed).grid(row=10, column=1, sticky=W, pady=4)


def registerBikeToShed():
    user = db.getUserByFirstAndLastName(firstName.get(), lastName.get())
    bike = db.addBikeToUser(user[0][0])
    print(bike)