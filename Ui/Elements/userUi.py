from tkinter import *

from Database import db

def registerUser(master):
    global firstName
    global insertion
    global lastName
    global address
    global zipCode
    global city

    Label(master, text="First Name").grid(row=0)
    Label(master, text="Middel Name").grid(row=1)
    Label(master, text="Last Name").grid(row=2)
    Label(master, text="Address").grid(row=3)
    Label(master, text="zip_code").grid(row=4)
    Label(master, text="city").grid(row=5)

    firstName = Entry(master)
    insertion = Entry(master)
    lastName = Entry(master)
    address = Entry(master)
    zipCode = Entry(master)
    city = Entry(master)

    firstName.grid(row=0, column=1)
    insertion.grid(row=1, column=1)
    lastName.grid(row=2, column=1)
    address.grid(row=3, column=1)
    zipCode.grid(row=4, column=1)
    city.grid(row=5, column=1)


    Button(master, text='Register', command=registerUserToDB).grid(row=6, column=1, sticky=W, pady=4)

def registerUserToDB():
    user = db.addUser(firstName.get(), insertion.get(), lastName.get(), address.get(), zipCode.get(), city.get())
    print(user)