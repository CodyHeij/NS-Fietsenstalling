from tkinter import *
from Database import db

# Lars van Kleef
def registerUser(master):
    '''Creates the ui for creating a user'''
    Message( master, text="Registreer een nieuwe gebruiker", width=200).grid(row=0, sticky=W, pady=4)

    # Using globals for the next function! I now :(
    global firstName
    global insertion
    global lastName
    global address
    global zipCode
    global city

    # Set the labels for the entry's
    Label(master, text="Voornaam").grid(row=1)
    Label(master, text="Tussen voegsel").grid(row=2)
    Label(master, text="Achternaam").grid(row=3)
    Label(master, text="Address").grid(row=4)
    Label(master, text="zip_code").grid(row=5)
    Label(master, text="city").grid(row=6)

    # set up the entry's
    firstName = Entry(master, width=50)
    insertion = Entry(master, width=50)
    lastName = Entry(master, width=50)
    address = Entry(master, width=50)
    zipCode = Entry(master, width=50)
    city = Entry(master, width=50)

    # Set the entry's into the grid
    firstName.grid(row=1, column=1)
    insertion.grid(row=2, column=1)
    lastName.grid(row=3, column=1)
    address.grid(row=4, column=1)
    zipCode.grid(row=5, column=1)
    city.grid(row=6, column=1)

    # Render a button for register the user
    Button(master, text='Register', command=registerUserToDB).grid(row=7, column=1, sticky=W, pady=4)

#Lars van Kleef
def registerUserToDB():
    # Try to add the user to the db
    try:
        user = db.addUser(firstName.get(), insertion.get(), lastName.get(), address.get(), zipCode.get(), city.get())
    except:
        print('Er is iets mis gegaan!')