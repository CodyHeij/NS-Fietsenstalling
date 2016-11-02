from tkinter import *

from Ui.Elements import userUi
from Ui.Elements import bikeUI
from Ui.Elements import shedUi

#Lars van Kleef
def main():
    '''Starts tkinter loop en creates ui'''
    master = Tk()
    userUi.registerUser(master)
    bikeUI.addBike(master)
    shedUi.addBike(master)
    shedUi.removeBike(master)
    mainloop()

#start the main UI
main()